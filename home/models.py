from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CASCADE, CharField, EmailField, ImageField, TextField, ForeignKey, SET_NULL
from django.utils.text import slugify


class User(AbstractUser):
    phone = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255, unique=True)
    image = ImageField(upload_to='image/', null=True, blank=True, max_length=255)
    info = TextField(null=True, blank=True)


class Category(Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'categoriya'
        verbose_name_plural = 'categoriyalar'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)


class Post(models.Model):
    author = ForeignKey('home.User', SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_post = models.ImageField()
    categories = models.ManyToManyField(Category, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

