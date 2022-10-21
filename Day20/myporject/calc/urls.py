
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("/arith", views.arith, name='arith'),
    path("/add", views.add, name='add'),
]