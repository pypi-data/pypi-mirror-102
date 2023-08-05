# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blickfeld/options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from .config import generate_pb2 as blickfeld_dot_config_dot_generate__pb2
from .config import secure_pb2 as blickfeld_dot_config_dot_secure__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='blickfeld/options.proto',
  package='blickfeld.protocol',
  syntax='proto2',
  serialized_options=_b('H\002'),
  serialized_pb=_b('\n\x17\x62lickfeld/options.proto\x12\x12\x62lickfeld.protocol\x1a google/protobuf/descriptor.proto\x1a\x1f\x62lickfeld/config/generate.proto\x1a\x1d\x62lickfeld/config/secure.proto:?\n\x0foptional_one_of\x12\x1d.google.protobuf.OneofOptions\x18\xd6\x86\x03 \x01(\x08:\x05\x66\x61lse:4\n\x05\x64_min\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\x01:\x04-inf:3\n\x05\x64_max\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x01:\x03inf:;\n\x06length\x12\x1d.google.protobuf.FieldOptions\x18\xd4\x86\x03 \x01(\x11:\n2147483647:2\n\x05regex\x12\x1d.google.protobuf.FieldOptions\x18\xd5\x86\x03 \x01(\t:\x02.*:8\n\x08optional\x12\x1d.google.protobuf.FieldOptions\x18\xd6\x86\x03 \x01(\x08:\x05\x66\x61lse:<\n\x0c\x61llow_sparse\x12\x1d.google.protobuf.FieldOptions\x18\xd7\x86\x03 \x01(\x08:\x05\x66\x61lse:6\n\nmin_length\x12\x1d.google.protobuf.FieldOptions\x18\xd8\x86\x03 \x01(\x11:\x01\x30:?\n\nmax_length\x12\x1d.google.protobuf.FieldOptions\x18\xd9\x86\x03 \x01(\x11:\n2147483647:8\n\x0flegacy_field_id\x12\x1d.google.protobuf.FieldOptions\x18\xda\x86\x03 \x01(\x04:-\n\x04unit\x12\x1d.google.protobuf.FieldOptions\x18\xdb\x86\x03 \x01(\t:0\n\x07ui_unit\x12\x1d.google.protobuf.FieldOptions\x18\xdc\x86\x03 \x01(\t:4\n\x08ui_scale\x12\x1d.google.protobuf.FieldOptions\x18\xdd\x86\x03 \x01(\x01:\x01\x31:=\n\x11ui_decimal_places\x12\x1d.google.protobuf.FieldOptions\x18\xde\x86\x03 \x01(\r:\x01\x30:]\n\x06\x65_desc\x12\x1f.google.protobuf.MessageOptions\x18\xe0\xd4\x03 \x01(\t:*No additional error description available.:1\n\x04help\x12\x1f.google.protobuf.MessageOptions\x18\xe1\xd4\x03 \x01(\t:\x00:T\n\x06secure\x12\x1f.google.protobuf.MessageOptions\x18\xe2\xd4\x03 \x01(\x0b\x32!.blickfeld.protocol.config.Secure:X\n\x08generate\x12\x1f.google.protobuf.MessageOptions\x18\xe3\xd4\x03 \x01(\x0b\x32#.blickfeld.protocol.config.GenerateB\x02H\x02')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,blickfeld_dot_config_dot_generate__pb2.DESCRIPTOR,blickfeld_dot_config_dot_secure__pb2.DESCRIPTOR,])


OPTIONAL_ONE_OF_FIELD_NUMBER = 50006
optional_one_of = _descriptor.FieldDescriptor(
  name='optional_one_of', full_name='blickfeld.protocol.optional_one_of', index=0,
  number=50006, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
D_MIN_FIELD_NUMBER = 50000
d_min = _descriptor.FieldDescriptor(
  name='d_min', full_name='blickfeld.protocol.d_min', index=1,
  number=50000, type=1, cpp_type=5, label=1,
  has_default_value=True, default_value=-1e10000,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
D_MAX_FIELD_NUMBER = 50001
d_max = _descriptor.FieldDescriptor(
  name='d_max', full_name='blickfeld.protocol.d_max', index=2,
  number=50001, type=1, cpp_type=5, label=1,
  has_default_value=True, default_value=1e10000,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
LENGTH_FIELD_NUMBER = 50004
length = _descriptor.FieldDescriptor(
  name='length', full_name='blickfeld.protocol.length', index=3,
  number=50004, type=17, cpp_type=1, label=1,
  has_default_value=True, default_value=2147483647,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
REGEX_FIELD_NUMBER = 50005
regex = _descriptor.FieldDescriptor(
  name='regex', full_name='blickfeld.protocol.regex', index=4,
  number=50005, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=_b(".*").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
OPTIONAL_FIELD_NUMBER = 50006
optional = _descriptor.FieldDescriptor(
  name='optional', full_name='blickfeld.protocol.optional', index=5,
  number=50006, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ALLOW_SPARSE_FIELD_NUMBER = 50007
allow_sparse = _descriptor.FieldDescriptor(
  name='allow_sparse', full_name='blickfeld.protocol.allow_sparse', index=6,
  number=50007, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MIN_LENGTH_FIELD_NUMBER = 50008
min_length = _descriptor.FieldDescriptor(
  name='min_length', full_name='blickfeld.protocol.min_length', index=7,
  number=50008, type=17, cpp_type=1, label=1,
  has_default_value=True, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MAX_LENGTH_FIELD_NUMBER = 50009
max_length = _descriptor.FieldDescriptor(
  name='max_length', full_name='blickfeld.protocol.max_length', index=8,
  number=50009, type=17, cpp_type=1, label=1,
  has_default_value=True, default_value=2147483647,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
LEGACY_FIELD_ID_FIELD_NUMBER = 50010
legacy_field_id = _descriptor.FieldDescriptor(
  name='legacy_field_id', full_name='blickfeld.protocol.legacy_field_id', index=9,
  number=50010, type=4, cpp_type=4, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
UNIT_FIELD_NUMBER = 50011
unit = _descriptor.FieldDescriptor(
  name='unit', full_name='blickfeld.protocol.unit', index=10,
  number=50011, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
UI_UNIT_FIELD_NUMBER = 50012
ui_unit = _descriptor.FieldDescriptor(
  name='ui_unit', full_name='blickfeld.protocol.ui_unit', index=11,
  number=50012, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
UI_SCALE_FIELD_NUMBER = 50013
ui_scale = _descriptor.FieldDescriptor(
  name='ui_scale', full_name='blickfeld.protocol.ui_scale', index=12,
  number=50013, type=1, cpp_type=5, label=1,
  has_default_value=True, default_value=float(1),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
UI_DECIMAL_PLACES_FIELD_NUMBER = 50014
ui_decimal_places = _descriptor.FieldDescriptor(
  name='ui_decimal_places', full_name='blickfeld.protocol.ui_decimal_places', index=13,
  number=50014, type=13, cpp_type=3, label=1,
  has_default_value=True, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
E_DESC_FIELD_NUMBER = 60000
e_desc = _descriptor.FieldDescriptor(
  name='e_desc', full_name='blickfeld.protocol.e_desc', index=14,
  number=60000, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=_b("No additional error description available.").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
HELP_FIELD_NUMBER = 60001
help = _descriptor.FieldDescriptor(
  name='help', full_name='blickfeld.protocol.help', index=15,
  number=60001, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
SECURE_FIELD_NUMBER = 60002
secure = _descriptor.FieldDescriptor(
  name='secure', full_name='blickfeld.protocol.secure', index=16,
  number=60002, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
GENERATE_FIELD_NUMBER = 60003
generate = _descriptor.FieldDescriptor(
  name='generate', full_name='blickfeld.protocol.generate', index=17,
  number=60003, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['optional_one_of'] = optional_one_of
DESCRIPTOR.extensions_by_name['d_min'] = d_min
DESCRIPTOR.extensions_by_name['d_max'] = d_max
DESCRIPTOR.extensions_by_name['length'] = length
DESCRIPTOR.extensions_by_name['regex'] = regex
DESCRIPTOR.extensions_by_name['optional'] = optional
DESCRIPTOR.extensions_by_name['allow_sparse'] = allow_sparse
DESCRIPTOR.extensions_by_name['min_length'] = min_length
DESCRIPTOR.extensions_by_name['max_length'] = max_length
DESCRIPTOR.extensions_by_name['legacy_field_id'] = legacy_field_id
DESCRIPTOR.extensions_by_name['unit'] = unit
DESCRIPTOR.extensions_by_name['ui_unit'] = ui_unit
DESCRIPTOR.extensions_by_name['ui_scale'] = ui_scale
DESCRIPTOR.extensions_by_name['ui_decimal_places'] = ui_decimal_places
DESCRIPTOR.extensions_by_name['e_desc'] = e_desc
DESCRIPTOR.extensions_by_name['help'] = help
DESCRIPTOR.extensions_by_name['secure'] = secure
DESCRIPTOR.extensions_by_name['generate'] = generate
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(optional_one_of)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(d_min)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(d_max)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(length)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(regex)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(optional)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(allow_sparse)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(min_length)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(max_length)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(legacy_field_id)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(unit)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(ui_unit)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(ui_scale)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(ui_decimal_places)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(e_desc)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(help)
secure.message_type = blickfeld_dot_config_dot_secure__pb2._SECURE
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(secure)
generate.message_type = blickfeld_dot_config_dot_generate__pb2._GENERATE
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(generate)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
