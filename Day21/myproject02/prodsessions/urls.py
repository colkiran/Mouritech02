
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='ssnhome'),
    path("setsession/", views.setsession, name='setsession'),
    path("getsession/", views.getsession, name='getsession'),
    path("deletesession/", views.deletesession, name='delsession'),
    path("setssntime/", views.setssntime, name='setssntime'),
    path("getssntime/", views.getssntime, name='getssntime'),
    path("delssntime/", views.deletessntime, name='delssntime')

]


