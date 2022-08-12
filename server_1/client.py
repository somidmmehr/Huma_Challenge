import grpc
from protos import account_pb2
from protos import account_pb2_grpc

print("hello")
with grpc.insecure_channel('localhost:50051') as channel:
    stub = account_pb2_grpc.UserControllerStub(channel)

    print('====== gRPC Create =======')
    response = stub.Create(account_pb2.User(username='new_user',
                                            email='new_user@django.grpc.com'))
    print(response, end='')

    print('====== gRPC List =======')
    for user in stub.List(account_pb2.UserListRequest()):
        print(user, end='')

    print('====== gRPC Retrieve =======')
    response = stub.Retrieve(account_pb2.UserRetrieveRequest(id=response.id))
    print(response, end='')

    print('====== gRPC Update =======')
    response = stub.Update(account_pb2.User(id=response.id,
                                            username='updated_user',
                                            email='updated_user@django.grpc.com'))
    print(response, end='')

    print('====== gRPC Delete =======')
    response = stub.Destroy(account_pb2.User(id=response.id))

