# Generated by Django 4.1 on 2022-09-17 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Category', models.CharField(choices=[('Choose item category', 'Choose item category'), ('Phones', 'Phones'), ('Accessories', 'Accessories'), ('Sneakers', 'Sneakers'), ('Others', 'Others')], default='Choose item category', max_length=50)),
                ('Description', models.CharField(max_length=500)),
                ('Location', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('Phone_num', models.CharField(max_length=15)),
                ('Quantity', models.PositiveIntegerField(default=1)),
                ('Address', models.TextField()),
                ('delivered', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.items')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
