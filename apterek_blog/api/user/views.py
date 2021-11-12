from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from api.user.serializers import RegisterUserSerializer, LoginUserSerializer, LogoutUserSerializer


class RegisterViewSet(CreateAPIView, viewsets.GenericViewSet):

    serializer_class = RegisterUserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"]
        )
        Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_201_CREATED)


class LoginView(CreateAPIView, viewsets.GenericViewSet):
    serializer_class = LoginUserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        token = Token.objects.get_or_create(user=user)[0].key
        return Response(status=status.HTTP_200_OK, data={"token": token})


class LogoutView(CreateAPIView, viewsets.GenericViewSet):

    serializer_class = LogoutUserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = logout(request)
        if user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)
