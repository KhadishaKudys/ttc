from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    categories_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name