
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("login/add", views.add, name='add'),
    path("delsession", views.delsession, name='delssn')
]