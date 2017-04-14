from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from .models import *
from .serializer import *
# Create your views here.

class ListUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSs


class DisplayUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSs
    lookup_field = 'id'

class ListUserDetails(ListAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSs


class DisplayUserDetails(RetrieveAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSs
    lookup_field = 'id'

class ListPost(ListAPIView):
    queryset = PostDetails.objects.all()
    serializer_class = PostDetailsSs


class DisplayPost(RetrieveAPIView):
    queryset = PostDetails.objects.all()
    serializer_class = PostDetailsSs
    lookup_field = 'id'

class ListCategories(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSs


class DisplayCategories(RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSs
    lookup_field = 'id'

class UserPost(ListAPIView):
    data = User.objects.filter(username = "harsh")
    user_id = data.values()[0]['id']
    queryset = PostDetails.objects.filter(user_id = user_id)
    serializer_class = PostDetailsSs
# class Update(UpdateAPIView):
#     queryset = UserDetails.objects.all()
#     serializer_class = UserDetailsSs
#     lookup_field = 'first_name'
#
# class Delete(DestroyAPIView):
#     queryset = UserDetails.objects.all()
#     serializer_class = UserDetailsSs
#     lookup_field = 'first_name'
#
# class Create(CreateAPIView):
#     queryset = UserDetails.objects.all()
#     serializer_class = UserCreateSerializer

