from django.db import models

# Create your models here. 

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=1000, null=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField()
    category = models.CharField(max_length=20)
    tags = models.JSONField(null=True)    