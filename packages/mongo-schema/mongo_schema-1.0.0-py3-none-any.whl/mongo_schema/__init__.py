"""jsonschema validator for MongoDB's JSON Schema extension."""


import copy
import datetime
import re
import warnings

import jsonschema


try:
    import bson
except ImportError:
    # We can use this package without the bson module installed, though a
    # warning will be raised when validing bsonType without it
    bson = None


__all__ = ['validate', 'MongoValidator']


__version__ = '1.0.0'


_BSON_TYPES = {
    'double': float,
    'string': str,
    'object': dict,
    'array': list,
    'binData': bytes,
    'undefined': None,
    'objectId': None,
    'bool': bool,
    'date': datetime.datetime,
    'null': type(None),
    'regex': type(re.compile('')),
    'dbPointer': None,
    'javascript': None,
    'symbol': None,
    'javascriptWithScope': None,
    'int': lambda x: isinstance(x, int) and -2**31 < x < 2**31 - 1,
    'timestamp': None,
    'long': lambda x: isinstance(x, int) and -2**63 < x < 2**63 - 1,
    # NOTE: Although a decimal.Decimal can be converted to a bson.Decimal128,
    # passing a decimal.Decimal directly is apparently not supported.
    'decimal': None,
    'minKey': None,
    'maxKey': None
}
"""
Mapping of bsonType names to equivalent Python types.

These mappings are informed by the documentation for the bson module:
https://pymongo.readthedocs.io/en/stable/api/bson/index.html

Note: Not all bsonTypes are mapped; only those that can be converted to from
Python using the bson module or Python built-in types.
"""


if bson is not None:
    _BSON_TYPES.update({
        'object': (dict, bson.SON),
        'bytes': (bytes, bson.Binary),
        'objectId': bson.ObjectId,
        'regex': (type(re.compile('')), bson.Regex),
        'dbPointer': bson.DBRef,
        # These are quite strict: javascriptWithScope *must* have a scope
        # even if it's an empty one, and javascript must *not* have a scope
        'javascript': lambda c: isinstance(c, bson.Code) and c.scope is None,
        'javascriptWithScope':
            lambda c: isinstance(c, bson.Code) and c.scope is not None,
        'timestamp': bson.Timestamp,
        'long': lambda x: (isinstance(x, (int, bson.Int64)) and
                           -2**63 < x < 2**63 - 1),
        'decimal': bson.Decimal128,
        'minKey': bson.MinKey,
        'maxKey': bson.MaxKey
    })


def bsonType(validator, types, instance, schema):
    """validator for the ``bsonType`` property"""

    if bson is None:
        warnings.warn(
            'the bson module must be installed in order to validate all '
            'bsonTypes; normally it is installed as part of PyMongo, though '
            'the stand-alone pybson package may also be used')

    types = [types] if not isinstance(types, list) else types

    def validate_bson_type(typ, instance):
        if typ not in _BSON_TYPES:
            raise jsonschema.ValidationError(
                f'{typ!r} is not a valid bsonType')

        validator = _BSON_TYPES[typ]
        if validator is None:
            raise jsonschema.ValidationError(
                f'{typ!r} does not have a Python equivalent in the bson '
                f'module and cannot be reprented by {instance!r}')
        elif isinstance(validator, (type, tuple)):
            def validator(inst, types=validator):
                # Special case for bool, which must be explicitly listed
                if isinstance(inst, bool) and bool not in types:
                    return False
                return isinstance(inst, types)

        return validator(instance)

    if not any(validate_bson_type(typ, instance) for typ in types):
        types = ', '.join(repr(typ) for typ in types)
        raise jsonschema.ValidationError(
                f'{instance!r} is not of type {types}')


# NOTE: As far as I can tell MongoDB does not explicitly publish a meta-schema;
# the schema definition is hard-coded at :
# https://github.com/mongodb/mongo/blob/5bbadc66ed462aed3cc4f5635c5003da6171c25d/src/mongo/db/matcher/schema/json_schema_parser.cpp
# It starts as a copy of the Draft 4 metaschema, but then drops various
# irrelevant or unsupported properties, extends it with the new definitions.
def _create_meta_schema():
    meta_schema = copy.deepcopy(jsonschema.Draft4Validator.META_SCHEMA)
    for key in ('id', 'description'):
        del meta_schema[key]

    # NOTE: although MongoDB explicitly does *not* support $ref, it is not
    # defined by the JSON Schema metaschema
    for prop in ('$schema', 'default', 'definitions', 'format', 'id'):
        del meta_schema['properties'][prop]

    # The 'type' property explicitly does not support 'integer'
    simple_types = meta_schema['definitions']['simpleTypes']['enum']
    meta_schema['definitions']['simpleTypes']['enum'] = [
        typ for typ in simple_types if typ != 'integer']

    # Define the bsonType property
    # NOTE: While all these types are supported by the schema format, not all
    # of them have Python equivalents
    # This list comes from
    # https://docs.mongodb.com/manual/reference/operator/query/type/#std-label-document-type-available-types
    meta_schema['definitions']['bsonTypes'] = {
        'enum': ['double', 'string', 'object', 'array', 'binData', 'undefined',
                 'objectId', 'bool', 'date', 'null', 'regex', 'dbPointer',
                 'javascript', 'symbol', 'javascriptWithScope', 'int',
                 'timestamp', 'long', 'decimal', 'minKey', 'maxKey', 'number']
    }
    meta_schema['properties']['bsonType'] = {
        'anyOf': [
            {'$ref': '#/definitions/bsonTypes'},
            {
                'type': 'array',
                'items': {'$ref': '#/definitions/bsonTypes'},
                'minItems': 1,
                'uniqueItems': True
            }
        ]
    }

    # MongoDB explicitly disallows unknown / custom schema properties
    meta_schema['additionalProperties'] = False

    return meta_schema


class MongoValidator(jsonschema.validators.create(
        meta_schema=_create_meta_schema(),
        validators=dict(bsonType=bsonType,
                        **jsonschema.Draft4Validator.VALIDATORS),
        type_checker=jsonschema.Draft4Validator.TYPE_CHECKER)):
    """Validator for MongoDB schemas."""


def validate(instance, schema, *args, **kwargs):
    """Validate the given document against a MongoDB schema."""
    return jsonschema.validate(instance, schema, cls=MongoValidator,
                               *args, **kwargs)
