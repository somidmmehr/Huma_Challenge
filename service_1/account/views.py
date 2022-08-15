import grpc
from grpc._channel import _InactiveRpcError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserSerializer
from protos import account_pb2_grpc, account_pb2


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            try:
                response = stub.List(account_pb2.UserListRequest())
            except _InactiveRpcError as exception:
                return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

            users = UserSerializer(response, many=True)
            return Response(users.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            try:
                response = stub.Create(account_pb2.User(username=request.data.get('username'),
                                                        email=request.data.get('email'),
                                                        password=request.data.get('password')))
            except _InactiveRpcError as exception:
                return Response(exception.details(), status=status.HTTP_406_NOT_ACCEPTABLE)

            user_serializer = UserSerializer(response)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            try:
                response = stub.Retrieve(account_pb2.UserRetrieveRequest(id=pk))
            except _InactiveRpcError as exception:
                return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

            user = UserSerializer(response)
            return Response(user.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            try:
                response = stub.Update(account_pb2.User(id=pk,
                                                        username=request.data.get('username'),
                                                        email=request.data.get('email')))
            except _InactiveRpcError as exception:
                return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

            user_serializer = UserSerializer(response)
            return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            try:
                stub.Destroy(account_pb2.UserRetrieveRequest(id=pk))
            except _InactiveRpcError as exception:
                return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

            return Response(None, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            grpc_request = account_pb2.UserRetrieveRequest()
            grpc_request.username.value = request.data.get('username')
            grpc_request.password.value = request.data.get('password')
            try:
                response = stub.Retrieve(grpc_request)
            except _InactiveRpcError as exception:
                return Response(exception.details(), status=status.HTTP_404_NOT_FOUND)

            user = UserSerializer(response)
            return Response(user.data, status=status.HTTP_200_OK)