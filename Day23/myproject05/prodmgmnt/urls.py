
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProdDisp, name="Prod"),
    path("products/AddProd", views.AddProd, name="AddProd"),
    path("EditProd/<int:id>", views.EditProd, name="EditProd"),
    path("EditProd/UpdateProd/<int:id>", views.UpdateProd, name='UpdateProd'),
]