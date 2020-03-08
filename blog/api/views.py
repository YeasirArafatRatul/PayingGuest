import datetime
from rest_framework import generics
from django.utils import timezone
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer, PostCreateSerializer


class PostapiView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer

    def create(self, request):
        data = self.request.data
        serializer = PostCreateSerializer(data=data)

        if serializer.is_valid():
            owner = self.request.user
            serializer.save(owner=owner, date_posted=timezone.now())
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PostDetailsAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
