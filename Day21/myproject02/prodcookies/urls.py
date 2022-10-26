
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name ='cookiehome'),
    path("setcookie/", views.setcookie, name='setcookie'),
    path("getcookie/", views.getcookie, name='getcookie'),
    path("deletecookie/", views.deletcookie, name='delcookie')
]