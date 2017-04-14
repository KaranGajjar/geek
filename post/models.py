from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')))
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    contact = models.IntegerField()
    qualification = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='media/image')
    birthdate = models.DateField()

    def __str__(self):
        return self.firstname

class Categories(models.Model):
    choice = {
        ('CMS' , 'CMS'),
        ('SEO', 'SEO'),
        ('OS', 'OS'),
        ('GAME', 'GAME'),
        ('LANGUAGE', 'LANGUAGE'),
        ('HOW_TO', 'HOW TO'),
    }
    cat_name = models.CharField(max_length=10,choices=choice)

    def __str__(self):
        return self.cat_name

class PostDetails(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    post_pic = models.ImageField(null=True)
    cat_id = models.ForeignKey(Categories)
    user_id = models.ForeignKey(User)
    user_name = models.ForeignKey(UserDetails)
    no_like = models.IntegerField(default=0)
    no_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title