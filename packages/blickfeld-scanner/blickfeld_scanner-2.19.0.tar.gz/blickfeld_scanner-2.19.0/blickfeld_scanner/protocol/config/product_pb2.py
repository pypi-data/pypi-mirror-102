# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blickfeld/config/product.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blickfeld/config/product.proto',
  package='blickfeld.protocol.config',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1e\x62lickfeld/config/product.proto\x12\x19\x62lickfeld.protocol.config*3\n\x07Product\x12\x10\n\x0cPRODUCT_CUBE\x10\x00\x12\x16\n\x12PRODUCT_CUBE_RANGE\x10\x02')
)

_PRODUCT = _descriptor.EnumDescriptor(
  name='Product',
  full_name='blickfeld.protocol.config.Product',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_CUBE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_CUBE_RANGE', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=61,
  serialized_end=112,
)
_sym_db.RegisterEnumDescriptor(_PRODUCT)

Product = enum_type_wrapper.EnumTypeWrapper(_PRODUCT)
PRODUCT_CUBE = 0
PRODUCT_CUBE_RANGE = 2


DESCRIPTOR.enum_types_by_name['Product'] = _PRODUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
