from django.contrib import admin
from .models import Menu
from .models import Chef
from .models import Klassyweek
from .models import Rezervation
from .models import Cart


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')   
 
admin.site.register(Menu,MenuAdmin)

class ChefAdmin(admin.ModelAdmin):
    list_display = ('id','name')   
 
admin.site.register(Chef,ChefAdmin)

class KlassyweekAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')   
 
admin.site.register(Klassyweek,KlassyweekAdmin)

class RezervationAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')   
 
admin.site.register(Rezervation,RezervationAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','product_name' , 'product_img', 'product_quantity' , 'product_price')   

admin.site.register(Cart , CartAdmin)
 


# Register your models here.
