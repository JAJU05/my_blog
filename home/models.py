from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CASCADE, CharField, EmailField, ImageField, TextField


class User(AbstractUser):
    phone = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255, unique=True)
    image = ImageField(upload_to='image/', null=True, blank=True, max_length=255)
    info = TextField(null=True, blank=True)


class Category(Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.ImageField()

    def __str__(self):
        return self.title