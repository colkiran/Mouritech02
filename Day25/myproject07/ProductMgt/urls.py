
from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_show, name="add"),
    path("updatedata/<int:id>", views.update_data, name="updatedata"),
    path("deletedata/<int:id>", views.delete_data, name="deletedata")
]