from django.shortcuts import render
from .models import Product
#from django.shortcuts import HttpResponse

# Create your views here.
"""
def index(request):
    return HttpResponse("<h1>Using shortcuts. My first webpage with python Django</h1>")
"""
def product_list(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request,'plpecommerce/product_list.html',context)
