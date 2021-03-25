from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.icecream_list, name='icecream-list'),
    path('<int:pk>/', views.icecream_detail)
]