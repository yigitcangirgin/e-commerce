from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm , TextInput
from project.models import Klassyweek , Menu

class ShopCart(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    product = models.ForeignKey(Klassyweek , on_delete=models.SET_NULL , null=True)
    image = models.CharField(max_length=500 ,verbose_name="Ürün Resimi" , null=True)
    quantity = models.IntegerField()

    def amount(self):
        return (self.quantity * self.product.price)

    def price(self):
        return (self.product.price)
        
    def get_img_path(self):
        return  '/images/'+ self.product_img

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']