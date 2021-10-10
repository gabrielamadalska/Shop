from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Category

# Create your views here.

def index(request):
    all_products = Products.objects.all() #jak select all z sql
    one = Products.objects.get(pk=2)
    cat = Products.objects.filter(category=1)
    cat_name = Category.objects.get(id=4)
    categories = Category.objects.all()
    null = Products.objects.filter(category__isnull=True)
    include = Products.objects.filter(description__contains='polish')





    return HttpResponse( include )
