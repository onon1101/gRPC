# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/hello_GRPC.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19protocol/hello_GRPC.proto\x12\x07grpcLab\")\n\x0cHelloGrpcReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\" \n\x0eHelloGrpcReply\x12\x0e\n\x06result\x18\x01 \x01(\t2E\n\x04\x42ili\x12=\n\tHelloGrpc\x12\x15.grpcLab.HelloGrpcReq\x1a\x17.grpcLab.HelloGrpcReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protocol.hello_GRPC_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOGRPCREQ']._serialized_start=38
  _globals['_HELLOGRPCREQ']._serialized_end=79
  _globals['_HELLOGRPCREPLY']._serialized_start=81
  _globals['_HELLOGRPCREPLY']._serialized_end=113
  _globals['_BILI']._serialized_start=115
  _globals['_BILI']._serialized_end=184
# @@protoc_insertion_point(module_scope)