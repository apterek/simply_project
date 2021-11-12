from rest_framework import serializers


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=4)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, min_length=8)


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=4)
    password = serializers.CharField(max_length=100, min_length=8)


class LogoutUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=4)
    password = serializers.CharField(max_length=100, min_length=8)