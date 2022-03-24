from django.urls import path

# import the vies file from the same directory
from . import views

# 1: we need a urlpattern list to hold the paths
urlpatterns =[
    path("", views.index, name="index"),
    path("/brian", views.brian, name="brian"),
    path("/patrick", views.patrick, name="patrick"),
    path("/<str:name>", views.greet,name="greet")
]