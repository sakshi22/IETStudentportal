from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.queryPage, name='queries'),
    path('delete-query/<str:qid>/', views.deleteQuery, name='delete-query'),
    path('query/<str:qid>/', views.query, name='query'),

]
