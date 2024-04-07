# Generated by Django 4.1.4 on 2023-01-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_shopcart_product2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='product2',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='image',
            field=models.CharField(max_length=500, null=True, verbose_name='Ürün Resimi'),
        ),
    ]
