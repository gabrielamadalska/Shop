from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Category

# Create your views here.

def index(request):
    #all_products = Products.objects.all() #jak select all z sql
    # one = Products.objects.get(pk=2)
    # cat = Products.objects.filter(category=1)
    # cat_name = Category.objects.get(id=4)
    categories = Category.objects.all()
    # null = Products.objects.filter(category__isnull=True)
    # include = Products.objects.filter(description__contains='polish')

    return HttpResponse( categories )

def category(request, id):

    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.name)

def product(request, id):
    product_user = Products.objects.get(pk=id)
    caption = "<h1>" + str(product_user.name) +"</h1>" + \
              "<p>"  + str(product_user.description) +"</p>" + \
              "<p>"+ str(product_user.price) + "</p>"

    return HttpResponse(caption)
