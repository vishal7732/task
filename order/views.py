from django.shortcuts import render
from product.models import Product, Category
from .forms import SaveAddress
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import Address
from .models import Orders

# Create your views here.
def checkout(request,slug):
    pro = Product.objects.filter(slug=slug)
    pro1 = Address.objects.filter(user=request.user.username)
    if request.method =='POST':
        Name = request.POST['Name']
        new_price = request.POST['new_price']
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Address_Line_1 = request.POST['Address_Line_1']
        Address_Line_2 = request.POST['Address_Line_2']
        City = request.POST['City']
        Phone = request.POST['Phone']

        od = Orders(product_name=Name,price=new_price,user=request.user.username,First_Name=First_Name,Last_Name=Last_Name,Address_Line_1=Address_Line_1,Address_Line_2=Address_Line_2,City=City,Phone=Phone)
        od.save()
        return render(request, "thanks.html")

    lis = {'pro':pro,'pro1':pro1}
    return render(request, "checkout.html",lis)

def Addaddress(request):
    if request.method =='POST':
        fm = SaveAddress(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['First_Name']
            ln = fm.cleaned_data['Last_Name']
            a1 = fm.cleaned_data['Address_Line_1']
            a2 = fm.cleaned_data['Address_Line_2']
            ci = fm.cleaned_data['City']
            ph = fm.cleaned_data['Phone']
            reg = Address(user=request.user.username,First_Name=fn,Last_Name=ln,Address_Line_1=a1,Address_Line_2=a2,City=ci,Phone=ph)
            fm.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        fm = SaveAddress()
    lis = {'form':fm}
    return render(request, "address.html",lis)