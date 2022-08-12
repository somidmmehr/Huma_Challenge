from django_grpc_framework import proto_serializers
from .models import CustomUser
from protos import account_pb2


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = CustomUser
        proto_class = account_pb2.User
        fields = ['id', 'username', 'email', 'groups']
