# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blickfeld/update/hardware.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .. import options_pb2 as blickfeld_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='blickfeld/update/hardware.proto',
  package='blickfeld.protocol.update',
  syntax='proto2',
  serialized_options=_b('H\002'),
  serialized_pb=_b('\n\x1f\x62lickfeld/update/hardware.proto\x12\x19\x62lickfeld.protocol.update\x1a\x17\x62lickfeld/options.proto\"`\n\x18partial_trenz_eeprom_msg\x12\x44\n\x10hardware_variant\x18\x03 \x01(\x0e\x32*.blickfeld.protocol.update.HardwareVariant\"5\n\x19partial_module_eeprom_msg\x12\x18\n\x10hardware_version\x18\x63 \x01(\t*\xaa\x01\n\x0fHardwareVariant\x12\x10\n\x0c\x41LL_HARDWARE\x10\x05\x12\x14\n\x10UNKNOWN_HARDWARE\x10\x06\x12\x0f\n\x0bNO_HARDWARE\x10\x07\x12\r\n\tCUBE_V0_2\x10\x00\x12\r\n\tCUBE_V0_3\x10\x01\x12\r\n\tCUBE_V1_0\x10\x04\x12\r\n\tAURORA_P3\x10\x03\x12\x0e\n\nAPOLLON_A0\x10\x02\x12\x12\n\x0e\x41POLLON_A1_BDU\x10\x08\x42\x02H\x02')
  ,
  dependencies=[blickfeld_dot_options__pb2.DESCRIPTOR,])

_HARDWAREVARIANT = _descriptor.EnumDescriptor(
  name='HardwareVariant',
  full_name='blickfeld.protocol.update.HardwareVariant',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL_HARDWARE', index=0, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_HARDWARE', index=1, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_HARDWARE', index=2, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUBE_V0_2', index=3, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUBE_V0_3', index=4, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUBE_V1_0', index=5, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AURORA_P3', index=6, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APOLLON_A0', index=7, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APOLLON_A1_BDU', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=241,
  serialized_end=411,
)
_sym_db.RegisterEnumDescriptor(_HARDWAREVARIANT)

HardwareVariant = enum_type_wrapper.EnumTypeWrapper(_HARDWAREVARIANT)
ALL_HARDWARE = 5
UNKNOWN_HARDWARE = 6
NO_HARDWARE = 7
CUBE_V0_2 = 0
CUBE_V0_3 = 1
CUBE_V1_0 = 4
AURORA_P3 = 3
APOLLON_A0 = 2
APOLLON_A1_BDU = 8



_PARTIAL_TRENZ_EEPROM_MSG = _descriptor.Descriptor(
  name='partial_trenz_eeprom_msg',
  full_name='blickfeld.protocol.update.partial_trenz_eeprom_msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hardware_variant', full_name='blickfeld.protocol.update.partial_trenz_eeprom_msg.hardware_variant', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=87,
  serialized_end=183,
)


_PARTIAL_MODULE_EEPROM_MSG = _descriptor.Descriptor(
  name='partial_module_eeprom_msg',
  full_name='blickfeld.protocol.update.partial_module_eeprom_msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hardware_version', full_name='blickfeld.protocol.update.partial_module_eeprom_msg.hardware_version', index=0,
      number=99, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=185,
  serialized_end=238,
)

_PARTIAL_TRENZ_EEPROM_MSG.fields_by_name['hardware_variant'].enum_type = _HARDWAREVARIANT
DESCRIPTOR.message_types_by_name['partial_trenz_eeprom_msg'] = _PARTIAL_TRENZ_EEPROM_MSG
DESCRIPTOR.message_types_by_name['partial_module_eeprom_msg'] = _PARTIAL_MODULE_EEPROM_MSG
DESCRIPTOR.enum_types_by_name['HardwareVariant'] = _HARDWAREVARIANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

partial_trenz_eeprom_msg = _reflection.GeneratedProtocolMessageType('partial_trenz_eeprom_msg', (_message.Message,), dict(
  DESCRIPTOR = _PARTIAL_TRENZ_EEPROM_MSG,
  __module__ = 'blickfeld.update.hardware_pb2'
  # @@protoc_insertion_point(class_scope:blickfeld.protocol.update.partial_trenz_eeprom_msg)
  ))
_sym_db.RegisterMessage(partial_trenz_eeprom_msg)

partial_module_eeprom_msg = _reflection.GeneratedProtocolMessageType('partial_module_eeprom_msg', (_message.Message,), dict(
  DESCRIPTOR = _PARTIAL_MODULE_EEPROM_MSG,
  __module__ = 'blickfeld.update.hardware_pb2'
  # @@protoc_insertion_point(class_scope:blickfeld.protocol.update.partial_module_eeprom_msg)
  ))
_sym_db.RegisterMessage(partial_module_eeprom_msg)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
