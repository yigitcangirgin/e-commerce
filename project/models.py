from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='menu')
    price = models.IntegerField(default=1000)

    def __str__(self):
        return self.name

    def get_img_path(self):
        return  '/images/'+ self.image

    


class Chef(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Name", default='gorden ramseyex')
    image = models.ImageField(upload_to='chef')
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Klassyweek(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    image = models.ImageField(upload_to='klassyweek')
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=1000)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, default=1)
    category = models.CharField(
        max_length=100, verbose_name="Category", default="dinner")

    def __str__(self):
        return self.name

    def get_img_path(self):
        return  '/media/klassyweek/'+ self.image
    


class Rezervation(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    email = models.EmailField(max_length=200, verbose_name="email", default="")
    phoneNumber = models.IntegerField(default=1, verbose_name="phoneNumber")
    people = models.IntegerField(default=1, verbose_name="people")
    date = models.CharField(max_length=200, verbose_name='Date')
    time = models.CharField(max_length=200 , verbose_name='Time')
    description = models.CharField(max_length=250, verbose_name="description")
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    product_name = models.CharField(max_length=100, verbose_name=" Ürün Adı")
    product_img = models.CharField(max_length=150, verbose_name=" Ürün Resimi")
    product_quantity = models.IntegerField(default=1, verbose_name="Ürün Adeti")
    product_price = models.IntegerField(default=1, verbose_name="Ürün Fiyatı")


    def __str__(self):
        return self.product_name    

    def get_img_path(self):
        return  '/media/klassyweek/'+ self.product_img

    def toplamtutar(self):
       hepsi = Cart.objects.all()
       
       getirici1 = Cart.objects.get(id = 14).product_price
       getirici2 = Cart.objects.get(id = 13).product_price  
       toplam = getirici1 + getirici2
       return toplam
    
    def delete(self):
        cart_d = Cart.objects.filter(product_name = self.product_name)
        cart_d.delete()

    

# Create your models here.

 # class Cart(models.Model):
     # Fields to store the user, products, and quantities
     #user = models.ForeignKey(User, on_delete=models.CASCADE)
     #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # quantity = models.PositiveIntegerField()