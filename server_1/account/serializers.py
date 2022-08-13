from protos import account_pb2
from django.contrib.auth import get_user_model
from django_grpc_framework import proto_serializers

User = get_user_model()


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = account_pb2.User
        fields = ['id', 'username', 'email', 'groups']
