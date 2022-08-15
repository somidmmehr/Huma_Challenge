from rest_framework import serializers
from account.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'groups']
        extra_kwargs = {
            'password': {'write_only': True}
        }