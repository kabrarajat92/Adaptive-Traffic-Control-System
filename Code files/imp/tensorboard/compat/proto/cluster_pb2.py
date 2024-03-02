# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/compat/proto/cluster.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/compat/proto/cluster.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_options=_b('\n\032org.tensorflow.distruntimeB\rClusterProtosP\001Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\370\001\001'),
  serialized_pb=_b('\n&tensorboard/compat/proto/cluster.proto\x12\x0btensorboard\"s\n\x06JobDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x05tasks\x18\x02 \x03(\x0b\x32\x1e.tensorboard.JobDef.TasksEntry\x1a,\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\".\n\nClusterDef\x12 \n\x03job\x18\x01 \x03(\x0b\x32\x13.tensorboard.JobDefBn\n\x1aorg.tensorflow.distruntimeB\rClusterProtosP\x01Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\xf8\x01\x01\x62\x06proto3')
)




_JOBDEF_TASKSENTRY = _descriptor.Descriptor(
  name='TasksEntry',
  full_name='tensorboard.JobDef.TasksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorboard.JobDef.TasksEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.JobDef.TasksEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=170,
)

_JOBDEF = _descriptor.Descriptor(
  name='JobDef',
  full_name='tensorboard.JobDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorboard.JobDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='tensorboard.JobDef.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_JOBDEF_TASKSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=170,
)


_CLUSTERDEF = _descriptor.Descriptor(
  name='ClusterDef',
  full_name='tensorboard.ClusterDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='tensorboard.ClusterDef.job', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=218,
)

_JOBDEF_TASKSENTRY.containing_type = _JOBDEF
_JOBDEF.fields_by_name['tasks'].message_type = _JOBDEF_TASKSENTRY
_CLUSTERDEF.fields_by_name['job'].message_type = _JOBDEF
DESCRIPTOR.message_types_by_name['JobDef'] = _JOBDEF
DESCRIPTOR.message_types_by_name['ClusterDef'] = _CLUSTERDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobDef = _reflection.GeneratedProtocolMessageType('JobDef', (_message.Message,), {

  'TasksEntry' : _reflection.GeneratedProtocolMessageType('TasksEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOBDEF_TASKSENTRY,
    '__module__' : 'tensorboard.compat.proto.cluster_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.JobDef.TasksEntry)
    })
  ,
  'DESCRIPTOR' : _JOBDEF,
  '__module__' : 'tensorboard.compat.proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.JobDef)
  })
_sym_db.RegisterMessage(JobDef)
_sym_db.RegisterMessage(JobDef.TasksEntry)

ClusterDef = _reflection.GeneratedProtocolMessageType('ClusterDef', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERDEF,
  '__module__' : 'tensorboard.compat.proto.cluster_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.ClusterDef)
  })
_sym_db.RegisterMessage(ClusterDef)


DESCRIPTOR._options = None
_JOBDEF_TASKSENTRY._options = None
# @@protoc_insertion_point(module_scope)