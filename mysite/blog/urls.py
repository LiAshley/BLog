from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:blog_id>', views.blog_post, name='blog_post'),
    path('blog_list.html/', views.blog_list, name='blog_list'),
    path('bootstrap.html/', views.bootstrap, name='bootstrap'),
    path('archives.html/', views.archives, name='archives'),
    path('django.html/', views.django, name='django'),
    path('waiting2.html/', views.waiting2, name='waiting2'),
    path('waiting3.html/', views.waiting3, name='waiting3'),
    path('waiting4.html/', views.waiting4, name='waiting4'),
]
