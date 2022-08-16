from rest_framework import serializers
from account.models import CustomUser
from protos import account_pb2
from django_grpc_framework import proto_serializers


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = CustomUser
        proto_class = account_pb2.User
        fields = ['id', 'username', 'email', 'password', 'groups']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if self.instance and (value == self.instance.email or value is None):
            return value

        if CustomUser.objects.filter(email=value).first():
            raise serializers.ValidationError("Email has been used before!")

        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        for group in groups:
            instance.groups.add(group)

        instance.save()
        return instance


class UserRetrieveProtoSerializer(UserProtoSerializer):
    def message_to_data(self, message):
        data = {
            'id': message.id,
        }
        if message.username.get('value'):
            data['username'] = message.username.value
        elif message.username.get('null'):
            data['username'] = None

        if message.password.get('value'):
            data['password'] = message.password.value
        elif message.password.get('null'):
            data['password'] = None

        return data