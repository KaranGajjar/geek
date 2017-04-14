from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSs(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

class UserDetailsSs(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"

class CategoriesSs(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"

class PostDetailsSs(serializers.ModelSerializer):
    class Meta:
        model = PostDetails
        fields = "__all__"
