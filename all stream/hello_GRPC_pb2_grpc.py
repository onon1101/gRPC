# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello_GRPC_pb2 as hello__GRPC__pb2


class BiliStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloGrpc = channel.unary_unary(
                '/grpcLab.Bili/HelloGrpc',
                request_serializer=hello__GRPC__pb2.HelloGrpcReq.SerializeToString,
                response_deserializer=hello__GRPC__pb2.HelloGrpcReply.FromString,
                )
        self.HelloTest = channel.stream_stream(
                '/grpcLab.Bili/HelloTest',
                request_serializer=hello__GRPC__pb2.HelloTestRequest.SerializeToString,
                response_deserializer=hello__GRPC__pb2.HelloTestResponse.FromString,
                )
        self.TestClientRecvStream = channel.unary_stream(
                '/grpcLab.Bili/TestClientRecvStream',
                request_serializer=hello__GRPC__pb2.TestClientRecvStreamRequest.SerializeToString,
                response_deserializer=hello__GRPC__pb2.TestClientRecvStreamResponse.FromString,
                )
        self.TestClientSendStream = channel.stream_unary(
                '/grpcLab.Bili/TestClientSendStream',
                request_serializer=hello__GRPC__pb2.TestClientSendStreamRequest.SerializeToString,
                response_deserializer=hello__GRPC__pb2.TestClientScendStreamResponse.FromString,
                )


class BiliServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HelloGrpc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HelloTest(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestClientRecvStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestClientSendStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BiliServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloGrpc': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloGrpc,
                    request_deserializer=hello__GRPC__pb2.HelloGrpcReq.FromString,
                    response_serializer=hello__GRPC__pb2.HelloGrpcReply.SerializeToString,
            ),
            'HelloTest': grpc.stream_stream_rpc_method_handler(
                    servicer.HelloTest,
                    request_deserializer=hello__GRPC__pb2.HelloTestRequest.FromString,
                    response_serializer=hello__GRPC__pb2.HelloTestResponse.SerializeToString,
            ),
            'TestClientRecvStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TestClientRecvStream,
                    request_deserializer=hello__GRPC__pb2.TestClientRecvStreamRequest.FromString,
                    response_serializer=hello__GRPC__pb2.TestClientRecvStreamResponse.SerializeToString,
            ),
            'TestClientSendStream': grpc.stream_unary_rpc_method_handler(
                    servicer.TestClientSendStream,
                    request_deserializer=hello__GRPC__pb2.TestClientSendStreamRequest.FromString,
                    response_serializer=hello__GRPC__pb2.TestClientScendStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcLab.Bili', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bili(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HelloGrpc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcLab.Bili/HelloGrpc',
            hello__GRPC__pb2.HelloGrpcReq.SerializeToString,
            hello__GRPC__pb2.HelloGrpcReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HelloTest(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/grpcLab.Bili/HelloTest',
            hello__GRPC__pb2.HelloTestRequest.SerializeToString,
            hello__GRPC__pb2.HelloTestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestClientRecvStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcLab.Bili/TestClientRecvStream',
            hello__GRPC__pb2.TestClientRecvStreamRequest.SerializeToString,
            hello__GRPC__pb2.TestClientRecvStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestClientSendStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/grpcLab.Bili/TestClientSendStream',
            hello__GRPC__pb2.TestClientSendStreamRequest.SerializeToString,
            hello__GRPC__pb2.TestClientScendStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)