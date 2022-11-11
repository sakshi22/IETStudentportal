from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('', views.home, name='home'),
    path('announcement/', views.announcement, name='announcement'),
    path('academic/', views.academic, name='academic'),

    path('post/<str:pid>/', views.post, name='post'),

    path('new-post/', views.newPost, name='new-post'),
    path('update-post/<str:pid>/', views.updatePost, name='update-post'),
    path('delete-post/<str:pid>/', views.deletePost, name='delete-post'),
    path('delete-comment/<str:cid>/', views.deleteComment, name='delete-comment'), 
]
