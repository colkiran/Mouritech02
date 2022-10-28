
from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.CarList.as_view())
]

