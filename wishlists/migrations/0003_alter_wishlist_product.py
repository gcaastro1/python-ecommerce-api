# Generated by Django 4.2 on 2023-05-05 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('wishlists', '0002_wishlist_product_wishlist_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='products.product'),
        ),
    ]
