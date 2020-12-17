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

    #Somewhere check if the REQUEST value is > 0, then put in e-mail

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
  #If the method is post
  if request.method == "POST":
    #Set the variable to the name of what each slot is
    namea = request.POST['namea']
    nameb = request.POST['nameb']
    namec = request.POST['namec']
    named = request.POST['named']
    namee = request.POST['namee']
    namef = request.POST['namef']
    nameg = request.POST['nameg']
    nameh = request.POST['nameh']
    namei = request.POST['namei']
    namej = request.POST['namej']
    namek = request.POST['namek']
    catername = request.POST['catername']

    #Passing as a request TO the order.html page
    return render(request, "main/order.html", { 
      #On the left is the name of the variable on the order page
      'nameA': namea, 
      'nameB': nameb,
      'nameC': namec,
      'nameD': named, 
      'nameE': namee,
      'nameF': namef,
      'nameG': nameg, 
      'nameH': nameh,
      'nameI': namei,
      'nameJ': namej, 
      'nameK': namek,
      'caterName': catername,
    })
  return render(request, "main/admin5959.html")

def send_email(request):
  return render(request, "main/send_email.html")