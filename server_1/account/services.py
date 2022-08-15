import grpc
from django_grpc_framework import generics
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from .models import CustomUser
from .serializers import UserProtoSerializer, UserRetrieveProtoSerializer


# class CustomUserService(generics.ModelService):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserProtoSerializer


class CustomUserService(Service):
    def List(self, request, context):
        user = CustomUser.objects.all()
        serializer = UserProtoSerializer(user, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = UserProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, f'User id {pk} not found!')

    def auth_object(self, username, password):
        user = CustomUser.objects.filter(username=username).first()
        if user is None:
            self.context.abort(grpc.StatusCode.NOT_FOUND, f'User by username {username} not found!')

        if not user.check_password(password):
            self.context.abort(grpc.StatusCode.NOT_FOUND, f'Incorrect password!')

        return user

    def Retrieve(self, request, context):
        if request.id == 0:
            user = self.auth_object(request.username.value, request.password.value)
        else:
            user = self.get_object(request.id)

        serializer = UserRetrieveProtoSerializer(user)
        return serializer.message

    def Update(self, request, context):
        user = self.get_object(request.id)
        serializer = UserProtoSerializer(user, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        user = self.get_object(request.id)
        user.delete()
        return empty_pb2.Empty()
