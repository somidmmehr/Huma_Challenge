import grpc
from protos import account_pb2
from protos import account_pb2_grpc

print("hello")
with grpc.insecure_channel('localhost:50051') as channel:
    stub = account_pb2_grpc.UserControllerStub(channel)
    for user in stub.List(account_pb2.UserListRequest()):
        print(user, end='')
