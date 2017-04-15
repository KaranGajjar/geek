from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .models import *
from .serializer import *
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get('un')
        password = request.POST.get('pw')
        user = auth.authenticate(username = username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(UserPost)
        else:
            return render(request,'login.html')
    return render(request, 'login.html')


@api_view(['GET','POST'])
def ListUser(request):
    queryset = User.objects.all()
    serializer = UserSs(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def DisplayUser(request):
    queryset = User.objects.all()
    serializer = UserSs(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def ListUserDetails(request):
    queryset = UserDetails.objects.all()
    serializer = UserDetailsSs(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def DisplayUserDetails(request):
    queryset = UserDetails.objects.all()
    serializer = UserDetailsSs(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def ListPosts(request):
    queryset = PostDetails.objects.all()
    serializer = PostDetailsSs(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def DisplayPosts(request):
    queryset = PostDetails.objects.all()
    serializer = PostDetailsSs(queryset, many=True)
    return Response(serializer.data)
@api_view(['GET','POST'])
def ListCategories(request):
    queryset = Categories.objects.all()
    serializer = CategoriesSs(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def DisplayCategories(request):
    queryset = Categories.objects.all()
    serializer = CategoriesSs(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def UserPost(request):
    if request.user.is_authenticated():
        user_id = request.user.id
        queryset = PostDetails.objects.filter(user_id = user_id)
        serializer = PostDetailsSs(queryset, many=True)
        return Response(serializer.data)
    else:
        return redirect(login)

