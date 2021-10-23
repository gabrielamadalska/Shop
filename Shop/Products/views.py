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
    data = {'categories' : categories}
    return render(request, 'szablon.html', data)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    category_product = Products.objects.filter(category = category_user)
    categories = Category.objects.all()
    data = {'category_user' : category_user,
            'category_product' : category_product,
            'categories': categories}
    return render(request, 'category_product.html', data)

def product(request, id):
    product_user = Products.objects.get(pk=id)
    categories = Category.objects.all()
    data = {'product_user' : product_user, 'categories' : categories}
    return render(request, 'product.html', data)


    #return HttpResponse(caption)


    # caption = "<h1>" + str(product_user.name) +"</h1>" + \
    #           "<p>"  + str(product_user.description) +"</p>" + \
    #           "<p>"+ str(product_user.price) + "</p>"


