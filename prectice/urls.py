"""prectice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from post.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/$',ListUser.as_view()),
    url(r'^user/(?P<id>[\w-]+)/$',DisplayUser.as_view()),
    url(r'^userd/$',ListUserDetails.as_view()),
    url(r'^userd/(?P<id>[\w-]+)/$',DisplayUserDetails.as_view()),
    url(r'^post/$',ListPost.as_view()),
    url(r'^post/(?P<id>[\w-]+)/$',DisplayPost.as_view()),
    url(r'^categories/$',ListCategories.as_view()),
    url(r'^categories/(?P<id>[\w-]+)/$',DisplayCategories.as_view()),
    url(r'^harsh/',UserPost.as_view())
]
