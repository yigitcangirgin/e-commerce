# Generated by Django 4.1.4 on 2023-01-06 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_cart'),
        ('order', '0002_alter_shopcart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='product2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.menu'),
        ),
    ]