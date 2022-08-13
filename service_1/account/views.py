import grpc
from grpc._channel import _InactiveRpcError
from rest_framework import viewsets, status
from rest_framework.response import Response
from account.serializers import UserSerializer
from protos import account_pb2_grpc, account_pb2


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = account_pb2_grpc.UserControllerStub(channel)
                response = stub.List(account_pb2.UserListRequest())
                users = UserSerializer(response, many=True)
                return Response(users.data, status=status.HTTP_200_OK)
        except _InactiveRpcError as exception:
            return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        try:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = account_pb2_grpc.UserControllerStub(channel)
                response = stub.Create(account_pb2.User(username=request.get('username'),
                                                        email=request.data.get('email')))
                user_serializer = UserSerializer(response)
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        except _InactiveRpcError as exception:
            return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = account_pb2_grpc.UserControllerStub(channel)
                response = stub.Retrieve(account_pb2.UserRetrieveRequest(id=pk))
                user = UserSerializer(response)
                return Response(user.data, status=status.HTTP_200_OK)
        except _InactiveRpcError as exception:
            return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        try:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = account_pb2_grpc.UserControllerStub(channel)
                response = stub.Update(account_pb2.User(id=pk,
                                                        username=request.data.get('username'),
                                                        email=request.data.get('email')))
                user_serializer = UserSerializer(response)
                return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
        except _InactiveRpcError as exception:
            return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = account_pb2_grpc.UserControllerStub(channel)
                response = stub.Destroy(account_pb2.UserRetrieveRequest(id=pk))
                user = UserSerializer(response)
                return Response(None, status=status.HTTP_200_OK)
        except _InactiveRpcError as exception:
            return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)
