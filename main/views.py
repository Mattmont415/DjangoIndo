from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


def index(request):
  return render(request, "main/index.html")

def menu(request):
  return render(request, "main/menu.html")

def order(request):
  return render(request, "main/order.html")