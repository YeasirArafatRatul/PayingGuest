import datetime
from rest_framework import generics
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
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
            serializer.save(owner=owner)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# class PostsUpdateApiView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


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
