import datetime
from rest_framework import generics
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from forms.models import User
from .serializers import UserSerializer, UserCreateSerializer


class UserRegistrationAPI(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request):
        data = self.request.data
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserDetailsAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
