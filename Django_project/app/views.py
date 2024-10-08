from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello world")

def signup(request):
    return HttpResponse("Signup Page")

def signin(request):
    return HttpResponse("Hooray you are in")