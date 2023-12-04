#coding:utf-8

import grpc
import hello_GRPC_pb2 as pb2
import hello_GRPC_pb2_grpc as pb2_grpc

def run():
    # 先定义一个频道
    conn = grpc.insecure_channel('localhost:5000')

    #设定客户端的频道
    client = pb2_grpc.BiliStub(channel=conn)

    # response是pb2.HelloGrpcReply类型
    response: pb2.HelloGrpcReply = client.HelloGrpc(pb2.HelloGrpcReq(
        name='Diamon',
        age=27
    ))
    print(response.result)

if __name__ == '__main__':
    run()