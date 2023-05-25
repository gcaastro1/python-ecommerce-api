# Generated by Django 4.2 on 2023-05-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=120)),
                ('number', models.CharField(max_length=20)),
                ('neighborhood', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=9)),
                ('state', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=50)),
                ('is_default', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
