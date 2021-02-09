from django.db import models


# Create your models here.

class CatagoryModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    catagory = models.ForeignKey(CatagoryModel,related_name='catagories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
