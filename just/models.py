from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100,blank=False)
    product_price = models.CharField(max_length=100,blank=False)
    category = models.CharField(max_length=100,blank=False)
    subcategory = models.CharField(max_length = 100,blank=False)
    manufacturer_detail = models.CharField(max_length=100,blank=True)
    seller_name = models.CharField(max_length=100,blank=True)
    desc = models.CharField(max_length =1000,blank=False)
    short_desc = models.CharField(max_length =500,blank=True,default="")
    warranty_period = models.CharField(max_length=1000,blank=False,default="")
    refundable = models.CharField(max_length=1000,blank=False,default="")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="shop/images")
    image1 = models.ImageField(upload_to="shop/images",blank=True)
    image2 = models.ImageField(upload_to="shop/images",blank=True)
    image3 = models.ImageField(upload_to="shop/images",blank=True)
    image4 = models.ImageField(upload_to="shop/images",blank=True)
    size1 = models.CharField(max_length=100,default="",blank=True)
    size2 = models.CharField(max_length=100,default="",blank=True)
    size3 = models.CharField(max_length=100,default="",blank=True)
    size4 = models.CharField(max_length=100,default="",blank=True)
    size5 = models.CharField(max_length=100,default="",blank=True)
    instock = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.product_name

class Users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(primary_key=True,max_length=100)
    password = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

class Contact(models.Model):
    contact_id = models.AutoField(primary_key = True)
    contact_name = models.CharField(max_length=200,default="")
    contact_number = models.CharField(max_length=200,default="")
    contact_email = models.CharField(max_length=200,default="")
    contact_date = models.DateTimeField(auto_now_add = True)
    msg = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.contact_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=100,default="")
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_image = models.CharField(max_length=100,default="")
    category_size = models.CharField(max_length=100,default="no size",blank=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=100)
    alternative_number = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=500)
    Alternate_address = models.CharField(max_length=500,blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=50)
    customer_username = models.CharField(max_length=500)
    status = models.CharField(max_length=100,default="Order Placed")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_username
    
    




