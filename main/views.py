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

    message = "You ordered " + request.POST['personal'] + " personal meals.\n" + "And " + request.POST['family'] + " family meals." + "The address to send is " + request.POST['address']
    # personal_meal = request.POST['personal']
    # family_meal = request.POST['family']

    send_mail(
      message_name, #Subject
      message, #Message itself
      "tonisfabkitchen@gmail.com", #from email
      ['mattmont415@gmail.com', 'tonisfabkitchen@gmail.com', message_email], #to email
    )

    return render(request, "main/send_email.html")

  return render(request, "main/order.html")



def about(request):
  return render(request, "main/about.html")

def admin5959(request):
  return render(request, "main/admin5959.html")

def send_email(request):
  return render(request, "main/send_email.html")