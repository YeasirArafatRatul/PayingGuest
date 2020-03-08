from rest_framework import serializers
from forms.models import User

# converting to json and validation for passed data+


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'phone',
                  'bio']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name',
                  'phone', 'bio', 'Address', 'Gender', ]
