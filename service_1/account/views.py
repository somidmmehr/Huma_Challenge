import grpc
from rest_framework import viewsets, status
from rest_framework.response import Response
from account.serializers import UserSerializer
from protos import account_pb2_grpc, account_pb2


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            response = stub.List(account_pb2.UserListRequest())
            users = UserSerializer(response, many=True)
            return Response(users.data, status=status.HTTP_200_OK)

    def create(self, request):
        return Response("create OK", status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = account_pb2_grpc.UserControllerStub(channel)
            response = stub.Retrieve(account_pb2.UserRetrieveRequest(id=pk))
            user = UserSerializer(response)
            return Response(user.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        return Response(f"update {pk} OK", status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        return Response(f"destroy {pk} OK", status=status.HTTP_200_OK)
