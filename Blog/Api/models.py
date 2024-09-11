from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)    

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=1000, null=False)
    created_at = models.DateField()
    update_at = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    