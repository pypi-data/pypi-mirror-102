# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blickfeld/status/imu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .. import options_pb2 as blickfeld_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='blickfeld/status/imu.proto',
  package='blickfeld.protocol.status',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x62lickfeld/status/imu.proto\x12\x19\x62lickfeld.protocol.status\x1a\x17\x62lickfeld/options.proto\"r\n\x03IMU\x12@\n\x0cstatic_state\x18\x01 \x01(\x0b\x32*.blickfeld.protocol.status.IMU.StaticState\x1a)\n\x0bStaticState\x12\x1a\n\x0c\x61\x63\x63\x65leration\x18\x01 \x03(\x02\x42\x04\xa0\xb5\x18\x06')
  ,
  dependencies=[blickfeld_dot_options__pb2.DESCRIPTOR,])




_IMU_STATICSTATE = _descriptor.Descriptor(
  name='StaticState',
  full_name='blickfeld.protocol.status.IMU.StaticState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='blickfeld.protocol.status.IMU.StaticState.acceleration', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\265\030\006'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=196,
)

_IMU = _descriptor.Descriptor(
  name='IMU',
  full_name='blickfeld.protocol.status.IMU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='static_state', full_name='blickfeld.protocol.status.IMU.static_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMU_STATICSTATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=196,
)

_IMU_STATICSTATE.containing_type = _IMU
_IMU.fields_by_name['static_state'].message_type = _IMU_STATICSTATE
DESCRIPTOR.message_types_by_name['IMU'] = _IMU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IMU = _reflection.GeneratedProtocolMessageType('IMU', (_message.Message,), dict(

  StaticState = _reflection.GeneratedProtocolMessageType('StaticState', (_message.Message,), dict(
    DESCRIPTOR = _IMU_STATICSTATE,
    __module__ = 'blickfeld.status.imu_pb2'
    # @@protoc_insertion_point(class_scope:blickfeld.protocol.status.IMU.StaticState)
    ))
  ,
  DESCRIPTOR = _IMU,
  __module__ = 'blickfeld.status.imu_pb2'
  # @@protoc_insertion_point(class_scope:blickfeld.protocol.status.IMU)
  ))
_sym_db.RegisterMessage(IMU)
_sym_db.RegisterMessage(IMU.StaticState)


_IMU_STATICSTATE.fields_by_name['acceleration']._options = None
# @@protoc_insertion_point(module_scope)
