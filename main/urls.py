from django.urls import path

from . import views


urlpatterns = [
  path("", views.index, name="index"),
  path("menu", views.menu, name="menu"),
  path("order", views.order, name="order"),
  path("about", views.about, name="about"),
  path("admin5959", views.admin5959, name="admin5959"),
  path("send_email", views.send_email, name="send_email")
]