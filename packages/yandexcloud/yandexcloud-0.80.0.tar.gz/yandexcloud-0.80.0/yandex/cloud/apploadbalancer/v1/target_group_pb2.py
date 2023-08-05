# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/apploadbalancer/v1/target_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/apploadbalancer/v1/target_group.proto',
  package='yandex.cloud.apploadbalancer.v1',
  syntax='proto3',
  serialized_options=b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2yandex/cloud/apploadbalancer/v1/target_group.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xb2\x02\n\x0bTargetGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tfolder_id\x18\x04 \x01(\t\x12H\n\x06labels\x18\x05 \x03(\x0b\x32\x38.yandex.cloud.apploadbalancer.v1.TargetGroup.LabelsEntry\x12\x38\n\x07targets\x18\x06 \x03(\x0b\x32\'.yandex.cloud.apploadbalancer.v1.Target\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"G\n\x06Target\x12\x14\n\nip_address\x18\x01 \x01(\tH\x00\x12\x11\n\tsubnet_id\x18\x03 \x01(\tB\x14\n\x0c\x61\x64\x64ress_type\x12\x04\xc0\xc1\x31\x01\x42z\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_TARGETGROUP_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=458,
)

_TARGETGROUP = _descriptor.Descriptor(
  name='TargetGroup',
  full_name='yandex.cloud.apploadbalancer.v1.TargetGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.folder_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targets', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.targets', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.apploadbalancer.v1.TargetGroup.created_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TARGETGROUP_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=458,
)


_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='yandex.cloud.apploadbalancer.v1.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='yandex.cloud.apploadbalancer.v1.Target.ip_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.apploadbalancer.v1.Target.subnet_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='address_type', full_name='yandex.cloud.apploadbalancer.v1.Target.address_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=460,
  serialized_end=531,
)

_TARGETGROUP_LABELSENTRY.containing_type = _TARGETGROUP
_TARGETGROUP.fields_by_name['labels'].message_type = _TARGETGROUP_LABELSENTRY
_TARGETGROUP.fields_by_name['targets'].message_type = _TARGET
_TARGETGROUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TARGET.oneofs_by_name['address_type'].fields.append(
  _TARGET.fields_by_name['ip_address'])
_TARGET.fields_by_name['ip_address'].containing_oneof = _TARGET.oneofs_by_name['address_type']
DESCRIPTOR.message_types_by_name['TargetGroup'] = _TARGETGROUP
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetGroup = _reflection.GeneratedProtocolMessageType('TargetGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TARGETGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.TargetGroup.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _TARGETGROUP,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.TargetGroup)
  })
_sym_db.RegisterMessage(TargetGroup)
_sym_db.RegisterMessage(TargetGroup.LabelsEntry)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.Target)
  })
_sym_db.RegisterMessage(Target)


DESCRIPTOR._options = None
_TARGETGROUP_LABELSENTRY._options = None
_TARGET.oneofs_by_name['address_type']._options = None
# @@protoc_insertion_point(module_scope)
