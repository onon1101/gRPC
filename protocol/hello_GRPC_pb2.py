# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello_GRPC.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10hello_GRPC.proto\x12\x0btest_stream\"\x18\n\x06Number\x12\x0e\n\x06number\x18\x01 \x01(\x05\"\x16\n\x05Reply\x12\r\n\x05reply\x18\x01 \x01(\t2J\n\x0bTest_Stream\x12;\n\x0cListFeatures\x12\x13.test_stream.Number\x1a\x12.test_stream.Reply\"\x00\x30\x01\x42\x37\n\x1bio.grpc.examples.routeguideB\x10Test_StreamProtoP\x01\xa2\x02\x03RTGb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_GRPC_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.routeguideB\020Test_StreamProtoP\001\242\002\003RTG'
  _globals['_NUMBER']._serialized_start=33
  _globals['_NUMBER']._serialized_end=57
  _globals['_REPLY']._serialized_start=59
  _globals['_REPLY']._serialized_end=81
  _globals['_TEST_STREAM']._serialized_start=83
  _globals['_TEST_STREAM']._serialized_end=157
# @@protoc_insertion_point(module_scope)