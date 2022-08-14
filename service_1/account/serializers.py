import grpc
from grpc._channel import _InactiveRpcError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from account.models import CustomUser
from protos import account_pb2_grpc, account_pb2

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class CustomAuthSerializer(AuthTokenSerializer):
    id = serializers.IntegerField(
        label=_("Id")
    )
    username = serializers.CharField(
        label=_("Username"),
        write_only=True
    )
    email = serializers.EmailField(
        label=_("Email"),
        trim_whitespace=False,
        write_only=True
    )
    password = serializers.CharField(
        required=False
    )

    def validate(self, attrs):
        id = attrs.get('id', 0)
        username = attrs.get('username')
        email = attrs.get('email')

        if not username or not email:
            msg = _('Must include "username" and "email".')
            raise serializers.ValidationError(msg, code='authorization')

        user = CustomUser.objects.filter(username=username, email=email).first()
        if not user:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = account_pb2_grpc.UserControllerStub(channel)
                try:
                    response = stub.Retrieve(account_pb2.UserRetrieveRequest(id=id))
                except _InactiveRpcError as exception:
                    raise serializers.ValidationError(exception.details, code='authorization')

                CustomUser.objects.create_user(username=response.username, email=response.email)
                msg = _(f'Unable to log in with provided credentials. use following info instead: '
                        f'username = {response.username} ,'
                        f'email = {response.email}')
                raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
