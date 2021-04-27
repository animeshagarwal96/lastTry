from django.shortcuts import render,redirect
from django.http import HttpResponse as httpresponse
from .models import Product,Users,Contact,Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def searchTheProduct(query,product):
    products = []
    for i in product:
        if query in i.product_name or query in i.category  or query in i.subcategory:
            products.append(i)
    return products

def searchTheProductforShow(query,product):
    products = []
    j = 0
    for i in product:
        if query in i.product_name or query in i.category  or query in i.subcategory:
            products.append(i)
            if len(products)==3:
                break
    return products

def index(request):
    product = Product.objects.filter(instock = 5)
    if not product:
        return render(request,'shop/index.html')
    category = Product.objects.values('category')
    cats = {item['category'] for item in category}
    allprods = []
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        allprods.append(prod)
    params = {"allprods":allprods}
    return render(request,'shop/index.html',params)
    # return render(request,'shop/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        print(name)
        contact = Contact(contact_name=name,contact_number=phone,contact_email=email,msg=query)
        contact.save()
        messages.success(request,"Your query has been recorded succesfully")
    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def search(request):
    if request.method == "GET":
        query = request.GET.get('search')
        product = Product.objects.all()
        products = searchTheProduct(query,product)
    length = len(products)
    
    return render(request,'shop/search.html',{'products':products,'length':length})

def checkout(request,id):
    if request.method=='POST':
        product_id = request.POST.get('id')
        product_name = request.POST.get('productname')
        product_price = request.POST.get('price')
        product_category = request.POST.get('category')
        if product_category == 'Garments':
            category_size = request.POST.get('size')
        elif product_category == 'Pants':
            category_size = request.POST.get('size2')
        else:
            category_size = ""
        customer_name = request.POST.get('name')
        customer_email = request.POST.get('email')
        customer_phone = request.POST.get('phone')
        alternative_number = request.POST.get('phone2')
        delivery_address = request.POST.get('address1')
        Alternate_address = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipCode = request.POST.get('zip')
        customer_username = request.user.username
        #check the conditions
        if city.lower() != 'kolkata' or state.lower() != 'west bengal':
            messages.error(request,'We dont deliver this product to your place')
            return redirect(request.path)
        order = Order(product_id=product_id,product_name=product_name,product_price=product_price,product_category=product_category,category_size=category_size,customer_name=customer_name,customer_email=customer_email,customer_phone=customer_phone,alternative_number=alternative_number,delivery_address=delivery_address,Alternate_address=Alternate_address,city=city,state=state,zipCode=zipCode,customer_username = customer_username)
        order.save()
        messages.success(request,'Your order has been placed successfully')
        return redirect('home')
    product = Product.objects.filter(product_id = id)
    if not request.user.is_authenticated:
        messages.error(request,'You are not logged in please logged in first in order to Place any orders')
    if len(product) > 0:
        return render(request,'shop/checkout.html',{"product":product})
    return httpresponse("404 error")

def product(request,id):
    product = Product.objects.filter(product_id=id)
    query = product[0].product_name.split(" ")[0]
    query = query.lower()
    allprods = Product.objects.all()
    products = searchTheProductforShow(query,allprods)
    
    return render(request,'shop/product.html',{'product':product,'products':products})

def handleSignup(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        #check the conditions is true
        userin = Users.objects.filter(email = email)
        if(len(userin) != 0):
            messages.error(request,'Email id already exist please choose another Email id')
            return redirect('home')
        if password1 != password2:
            messages.error(request,'Passwords do not Match!!')
            return redirect('home')
        if len(password1) < 8:
            messages.error(request,'Password is too small')
            return redirect('home')
        #if all ok continue
        try:
            myuser = User.objects.create_user(email,email,password1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            user = Users(fname=fname,lname=lname,email=email,password=password1)
            user.save()
            # redirect('home')
            subject = 'welcome to JCNP world'
            message = f'Hi {myuser.first_name}, thank you for registering in JustClickNPick your register id is {myuser.email} and Password is {password1}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [myuser.email, ]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'Your Acount has been Registered')
            return redirect('home')
        except Exception as e:
            print(e)
            messages.error(request,'server error occur try again after some time')
            return redirect('home')
        return redirect('home')
    else: 
        return httpresponse('404 Error')


def handleLogin(request):
    if request.method == "POST":
        login_email = request.POST['loginemail']
        login_password = request.POST['loginpassword']
        
        user = authenticate(username=login_email, password=login_password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('home')
    else:
        return httpresponse('404 - not found')

def handleLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Successfully logged out')
        return redirect('home')
    else:
        return httpresponse('404 error')

def order(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(customer_username=request.user.username)
        imageList = []
        for i in orders:
            imageList.append(Product.objects.filter(product_id=i.product_id))
        allorders = ([orders,imageList])
        return render(request,'shop/order.html',{"orders":orders})
    else:
        messages.warning(request,'You are not logged in please logged in first in order to see your orders')
        return render(request,'shop/order.html')
        