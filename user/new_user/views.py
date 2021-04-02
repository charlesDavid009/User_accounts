from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .serializers import (UserSerializer,
UserCreateSerializer
)
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.


class BlogActionView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    # - Returns a serializer instance.
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            telephone = data.get('telephone')
            role = data.get('role')
            user_obj = User.objects.create_user(username=username,
                                                email=email,
                                                telephone=telephone,
                                                role=role
                                                )
            user_obj.set_password(password)
            serializers = user_obj.save()
            return Response(serializers, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

