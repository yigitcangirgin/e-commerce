from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from .models import Chef
from .models import Klassyweek
from .models import Rezervation
from accounts.views import *
from django.contrib import auth
from .models import Cart
from order.models import ShopCart , ShopCartForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu})


def chef(request):
    chef = Chef.objects.all()
    return render(request, 'chef.html', {'chef': chef})


def klassyweek(request):
    klassyweek = Klassyweek.objects.all()
    return render(request, 'klassyweek.html', {'klassyweek': klassyweek})


def contactus(request):
    rezervations = Rezervation.objects.all()
    user = auth.get_user(request)
    stranger = str(user)
    if request.method == 'POST':
        if stranger != "AnonymousUser":
            name = request.POST['name']
            email = request.POST['email']
            phoneNumber = request.POST['phoneNumber']
            people = request.POST['people']
            date = request.POST['date']
            time = request.POST['time']
            description = request.POST['description']
            rezervation = Rezervation(name=name, email=email, phoneNumber=phoneNumber,people=people, date=date, time=time, description=description)
            rezervation.save()
            return render(request, 'contactus.html', {'rezervations': rezervations, 'message': "Your reservation has been made successfully"})
        if 1==1:
            return render(request, 'contactus.html', {'rezervations': rezervations, 'error': "Hata"})
    return render(request, 'contactus.html', {'rezervations': rezervations})

   # def cart_add(request, product_id):
    cart = Cart(request)  # Create a cart object
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')

# ekle = Cart.objects.create(product_name = 'ek' , product_img='adasdas', product_quantity = 11 , product_price = 11)
# ekle.save()
def basket(request):
    klassyweek = Klassyweek.objects.all()
    current_user = request.user
    carts = Cart.objects.all()
    products = ShopCart.objects.all()
    schopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity
        
    context = {
        'carts' : carts ,
        'products' : products,
        'total' : total ,
        'klassyweek' : klassyweek,
    }
    return render(request, 'basket.html' , context)


