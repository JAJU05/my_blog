from django.urls import path, include
from django.conf import settings
from os import path

from views import homepage, post, about, allposts

urlpatterns = [
    path('', homepage, name='homepage'),
    path('post/<slug>/', post, name='post'),
    path('about/', about, name='about'),
    path('posts/', allposts, name='allposts'),
]