from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('hello', views.mainpage),
]
