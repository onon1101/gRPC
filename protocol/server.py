#coding:utf-8
import grpc
import hello_GRPC_pb2 as pb2
import hello_GRPC_pb2_grpc as pb2_grpc
import time
from concurrent import futures #多线程

class Bili(pb2_grpc.BiliServicer):#和proto文件中花括号外的Bili一致
    def HelloGrpc(self, request, context):
        name = request.name
        age = request.age

        result = f'my name is {name}, i am {age} years old'#f表示字串内支持大括号的表达式
        return pb2.HelloGrpcReply(result = result)

#启动服务
def run():
##1. 实例化server
    # 最大的线程数量
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
##2. 注册逻辑到server中
    #注册Bili这个类到GRPC里面,传入的第一个参数就是Bili()的实例化对象
    pb2_grpc.add_BiliServicer_to_server(Bili(),grpc_server)
    #绑定ip(这里一定要用insecure_port)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server will start at 0.0.0.0:5000')
#3. 启动server
    grpc_server.start()

    #用循环让它一直运行，直到有键盘输入退出服务
    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)
#也可以直接用grpc_server.wait_for_termination()让线程等待

if __name__ == '__main__':
    run()