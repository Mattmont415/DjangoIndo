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

    message = "Thank you for ordering with us!\n"
    message += "You ordered: \n"
    # if request.POST['namea'].value > 0:
    #   message += nameA + "\n"
    #   message += "Quantity: " + request.POST['namea'].value + "\n"
    #   message += "Total for item: " + (request.POST['namea'] * priceA)
    # personal_meal = request.POST['personal']
    # family_meal = request.POST['family']
    message += "Your order will come to: \n"
    message += request.POST['address']

    send_mail(
      message_name, #Subject
      message, #Message itself
      "tonisfabkitchen@gmail.com", #from email
      ['mattmont415@gmail.com', 'alexchen9333@gmail.com', 'tonisfabkitchen@gmail.com', message_email], #to email
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
    # nameb = request.POST['nameb']
    # namec = request.POST['namec']
    # named = request.POST['named']
    # namee = request.POST['namee']
    # namef = request.POST['namef']
    # nameg = request.POST['nameg']
    # nameh = request.POST['nameh']
    # namei = request.POST['namei']
    # namej = request.POST['namej']
    # namek = request.POST['namek']
    # catername = request.POST['catername']
    # pricea = request.POST['pricea']
    # priceb = request.POST['priceb']
    # pricec = request.POST['pricec']
    # priced = request.POST['priced']
    # pricee = request.POST['pricee']
    # pricef = request.POST['pricef']
    # priceg = request.POST['priceg']
    # priceh = request.POST['priceh']
    # pricei = request.POST['pricei']
    # pricej = request.POST['pricej']
    # pricek = request.POST['pricek']
    # caterprice = request.POST['caterprice']

    #Passing as a request TO the order.html page
    return render(request, "main/order.html", { 
    # return HttpResponseRedirect(reverse("order", kwargs= {
      #On the left is the name of the variable on the order page
      'nameA': namea, 
      # 'nameB': nameb,
      # 'nameC': namec,
      # 'nameD': named, 
      # 'nameE': namee,
      # 'nameF': namef,
      # 'nameG': nameg, 
      # 'nameH': nameh,
      # 'nameI': namei,
      # 'nameJ': namej, 
      # 'nameK': namek,
      # 'caterName': catername,
      # 'priceA': pricea,
      # 'priceB': priceb,
      # 'priceC': pricec,
      # 'priceD': priced,
      # 'priceE': pricee,
      # 'priceF': pricef,
      # 'priceG': priceg,
      # 'priceH': priceh,
      # 'priceI': pricei,
      # 'priceJ': pricej,
      # 'priceK': pricek,
      # 'caterPrice': caterprice
    })#) 
    #Uncomment for switching to HttpRespRedir

  #Need to keep this here so it's on the page it's supposed to be on, but how to redirect?
  return render(request, "main/admin5959.html")

def send_email(request):
  return render(request, "main/send_email.html")