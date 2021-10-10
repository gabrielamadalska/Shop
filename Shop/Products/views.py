from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.

def index(request):
    my_request = Products.objects.all() #jak select all z sql
    return HttpResponse(my_request)
