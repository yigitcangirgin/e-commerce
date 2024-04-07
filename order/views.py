from django.shortcuts import render 
from order.models import ShopCart ,ShopCartForm
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from .models import Menu
# Create your views here.
def index(request):
    return render(request , "basket.html")

def addtocart(request , id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method =='POST':
        form = ShopCartForm(request.POST)
        if True:
            current_user = request.user
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.image = 23423
            data.quantity = 1 
            data.save()
            messages.success(request , 'Ürün Başarılı')
        return HttpResponseRedirect(url)

def deletefromcart(request, id):
    url = request.META.get('HTTP_REFERER')
    deleted_product = ShopCart.objects.filter(id = id)
    deleted_product.delete()
    messages.success(request , "ÜRÜN SİLİNDİ")
    return HttpResponseRedirect(url)


def addtocart2(request , id):
    url = request.META.get('HTTP_REFERER')
    if request.method =='POST':
        form = ShopCartForm(request.POST)
        if True:
            current_user = request.user
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            
            data.quantity = 1
            data.save()
            messages.success(request , 'Ürün Başarılı')
            
        return HttpResponseRedirect(url)

def upgradefromcart(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method =='POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.image = " "
            data1 = ShopCart.objects.filter(id = id)
            print(data1)
            for item in data1:
                item.quantity += 1
                item.save()
            messages.success(request , 'Ürün Başarılı')

    
       
            
        return HttpResponseRedirect(url)

def lessfromcart(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method =='POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.image = " "
            data1 = ShopCart.objects.filter(id = id)
            print(data1)
            for item in data1:
                item.quantity -= 1
                if item.quantity <= 1:
                    pass
                if item.quantity > 0:
                    item.save()
                
            messages.success(request , 'Ürün Başarılı')

    
       
            
        return HttpResponseRedirect(url)