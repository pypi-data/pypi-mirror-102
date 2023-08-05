# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dmi/commons.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dmi/commons.proto',
  package='dmi',
  syntax='proto3',
  serialized_options=b'Z9github.com/opencord/device-management-interface/v3/go/dmi',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x64mi/commons.proto\x12\x03\x64mi*?\n\x06Status\x12\x14\n\x10UNDEFINED_STATUS\x10\x00\x12\r\n\tOK_STATUS\x10\x01\x12\x10\n\x0c\x45RROR_STATUS\x10\x02*?\n\x08LogLevel\x12\t\n\x05TRACE\x10\x00\x12\t\n\x05\x44\x45\x42UG\x10\x01\x12\x08\n\x04INFO\x10\x02\x12\x08\n\x04WARN\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x42;Z9github.com/opencord/device-management-interface/v3/go/dmib\x06proto3'
)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='dmi.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_STATUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK_STATUS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_STATUS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=26,
  serialized_end=89,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_LOGLEVEL = _descriptor.EnumDescriptor(
  name='LogLevel',
  full_name='dmi.LogLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRACE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=91,
  serialized_end=154,
)
_sym_db.RegisterEnumDescriptor(_LOGLEVEL)

LogLevel = enum_type_wrapper.EnumTypeWrapper(_LOGLEVEL)
UNDEFINED_STATUS = 0
OK_STATUS = 1
ERROR_STATUS = 2
TRACE = 0
DEBUG = 1
INFO = 2
WARN = 3
ERROR = 4


DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['LogLevel'] = _LOGLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
