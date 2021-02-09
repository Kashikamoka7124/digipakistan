from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class UserModel(models.Model):
    username = models.CharField(unique=True,null=False,max_length=50)
    email = models.EmailField(unique=True,null=False,blank=False)
    password = models.CharField(max_length=50,null=False,unique=True,blank=False)
    role = models.ForeignKey(Role,null=False,blank=False, on_delete=models.CASCADE)


class ProfileModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    address = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500,null=True)
    contact_no = models.CharField(max_length=12)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class CourseModel(models.Model):

    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(User,on_delete= models.CASCADE,related_name='teacher_id')
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ArticleModel(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField()
    discription = models.CharField(max_length=700)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogModel(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField()
    discription = models.CharField(max_length=700)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class EventModel(models.Model):
    
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=700,null=True)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CallobrationsModel(models.Model):    
    pass

class OnlineTestModel(models.Model):
    pass


class QueriesModel(models.Model):
    pass