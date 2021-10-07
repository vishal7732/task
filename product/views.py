from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def home(request):
    pro = Product.objects.all()
    cat = Category.objects.all()

    lis = {'pro':pro,'cat':cat}
    return render(request, "index.html",lis)

def prod(request,slug):
    pro = Product.objects.filter(slug=slug)

    lis = {'pro':pro}
    return render(request, "product.html",lis)

