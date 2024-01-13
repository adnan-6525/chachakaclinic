from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.data, name="data"),
    path("search/", views.search, name="search"),
    path("delete/<int:id>", views.delete, name="delete"),
]
