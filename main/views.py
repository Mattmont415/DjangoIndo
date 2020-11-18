from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.core.mail import send_mail




def index(request):
  return render(request, "main/index.html")

def menu(request):
  return render(request, "main/menu.html")

def order(request):
  if request.method == "POST":
    message_name = "Toni's Kitchen! Regarding order number: " #Need to get the order num some how
    message_email = request.POST['email']

    message = "You ordered " + request.POST['personal'] + " personal meals.\n" + "And " + request.POST['family'] + " meals."
    # personal_meal = request.POST['personal']
    # family_meal = request.POST['family']

    send_mail(
      message_name, #Subject
      message, #Message itself
      message_email, #from email
      ['mattmont415@gmail.com'], #to email
    )
  return render(request, "main/order.html")



def about(request):
  return render(request, "main/about.html")