# Generated by Django 4.2 on 2023-05-05 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_alter_cart_owner'),
        ('products', '0002_initial'),
        ('carts_products', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_list', to='carts.cart'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='products.product'),
        ),
    ]