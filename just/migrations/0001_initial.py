# Generated by Django 3.1.7 on 2021-04-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(default='', max_length=200)),
                ('contact_number', models.IntegerField(default='')),
                ('contact_email', models.CharField(default='', max_length=200)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('msg', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.CharField(default='', max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_category', models.CharField(max_length=100)),
                ('category_size', models.CharField(default='no size', max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=100)),
                ('alternative_number', models.CharField(max_length=100)),
                ('delivery_address', models.CharField(max_length=500)),
                ('Alternate_address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipCode', models.CharField(max_length=50)),
                ('customer_username', models.CharField(max_length=500)),
                ('status', models.CharField(default='Order Placed', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('manufacturer_detail', models.CharField(blank=True, max_length=100)),
                ('seller_name', models.CharField(blank=True, max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('short_desc', models.CharField(blank=True, default='', max_length=500)),
                ('warranty_period', models.CharField(default='', max_length=1000)),
                ('refundable', models.CharField(default='', max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='shop/images')),
                ('image1', models.ImageField(blank=True, upload_to='shop/images')),
                ('image2', models.ImageField(blank=True, upload_to='shop/images')),
                ('image3', models.ImageField(blank=True, upload_to='shop/images')),
                ('image4', models.ImageField(blank=True, upload_to='shop/images')),
                ('instock', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
