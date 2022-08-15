from rest_framework import serializers
from account.models import CustomUser
from protos import account_pb2
from django.contrib.auth import get_user_model
from django_grpc_framework import proto_serializers

User = get_user_model()


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = account_pb2.User
        fields = ['id', 'username', 'email', 'groups']

    def validate(self, attrs):
        if CustomUser.objects.filter(email=attrs.get('email')).first():
            raise serializers.ValidationError("Email has been used before!")

        return attrs

    def message_to_data(self, message):
        data = {
            'id': message.id,
        }
        if message.username.HasField('value'):
            data['username'] = message.username.value
        elif message.username.HasField('null'):
            data['username'] = None

        if message.password.HasField('value'):
            data['password'] = message.password.value
        elif message.password.HasField('null'):
            data['password'] = None

        return data