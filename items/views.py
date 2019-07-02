from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def index(Request):
    return HttpResponse("You're in the Items page.")

def show(Request):
    return HttpResponse("You're in the Items/show page.")

