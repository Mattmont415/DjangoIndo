from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("", views.menu, name="menu"),
  path("order", views.order, name="order")
]