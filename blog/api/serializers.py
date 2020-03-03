from rest_framework import serializers
from blog.models import Post

# converting to json and validation for passed data+


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['owner', 'place', 'title',
                  'price', 'description', 'date_posted', 'post_image']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['place', 'title',
                  'price', 'description', 'post_image']
