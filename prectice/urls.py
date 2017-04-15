"""prectice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home, name='home')
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
    url(r'^login/', login),
    url(r'^user/$',ListUser),
    url(r'^user/(?P<id>[\w-]+)/$',DisplayUser),
    url(r'^userd/$',ListUserDetails),
    url(r'^userd/(?P<id>[\w-]+)/$',DisplayUserDetails),
    url(r'^post/$',ListPosts),
    url(r'^post/(?P<id>[\w-]+)/$',DisplayPosts),
    url(r'^categories/$',ListCategories),
    url(r'^categories/(?P<id>[\w-]+)/$',DisplayCategories),
    url(r'^postd/',UserPost)
]
