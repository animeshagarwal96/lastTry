from django.shortcuts import render,redirect
from django.http import HttpResponse as httpresponse
from .models import Product,Users,Contact,Order,ProductComment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def searchTheProduct(query,product):
    products = []
    for i in product:
        if query in i.product_name.lower() or query in i.category.lower()  or query in i.subcategory.lower():
            products.append(i)
    return products

def searchTheProductforShow(query,product):
    products = []
    j = 0
    for i in product:
        if query in i.product_name.lower() or query in i.category.lower()  or query in i.subcategory.lower():
            products.append(i)
            if len(products)==3:
                break
    return products
    
def shop(request):
    product = Product.objects.all()
    if not product:
        return render(request,'shop/index.html')
    subcategory = Product.objects.values('subcategory')
    cats = {item['subcategory'] for item in subcategory}
    allprods = []
    for cat in cats:
        prod = Product.objects.filter(subcategory=cat,instock__gte = 1)
        allprods.append(prod)
    params = {"allprods":allprods}
    return render(request,'shop/home.html',params)

def index(request):
    product = Product.objects.all()
    if not product:
        return render(request,'shop/index.html')
    subcategory = Product.objects.values('subcategory')
    cats = {item['subcategory'] for item in subcategory}
    allprods = []
    for cat in cats:
        prod = Product.objects.filter(subcategory=cat,instock__gte = 1)
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
        if len(query) == 0:
            messages.info(request,"Cannot search an Empty field")
            return redirect(request.META.get('HTTP_REFERER'))
        product = Product.objects.filter(instock__gte = 1)
        products = searchTheProduct(query.lower(),product)
    length = len(products)
    
    return render(request,'shop/search.html',{'products':products,'length':length})

def checkout(request,id):
    if request.method=='POST':
        product = Product.objects.filter(product_id = id)
        product_id = product[0].product_id
        product_name = product[0].product_name
        product_price = product[0].product_price
        product_category = product[0].category
        product_quantity = request.POST.get('quantity1')
        image = product[0].image
        total_price = int(product_price) * int(product_quantity)
        if product_category == 'Garments' or product_category=='Pants' or product_category =='Kurti':
            category_size = request.POST.get('size')
        else:
            category_size = ""
        customer_name = request.POST.get('name')
        customer_email = request.POST.get('email1')
        customer_phone = request.POST.get('phone')
        alternative_number = request.POST.get('phone2')
        delivery_address = request.POST.get('address1')
        Alternate_address = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipCode = request.POST.get('zip')
        customer_username = request.user.username
        customer_firstName = request.user.first_name
        #check the conditions
        if city.lower() != 'kolkata' or state.lower() != 'west bengal':
            messages.error(request,'We dont deliver this product to your place')
            return redirect(request.path)
        order = Order(product_id=product_id,product_name=product_name,product_price=product_price,product_category=product_category,quantity=product_quantity,image=image,total_price=total_price,category_size=category_size,customer_name=customer_name,customer_email=customer_email,customer_phone=customer_phone,alternative_number=alternative_number,delivery_address=delivery_address,Alternate_address=Alternate_address,city=city,state=state,zipCode=zipCode,customer_username = customer_username)
        order.save()
        try:
            #Mail Owner
            subject = 'Order From JC&P'
            message = f'Hi Mr Rahul, there is a Order placed by {request.user.first_name} with product {product_name}({product_quantity}) of Amount Rs {total_price} from JustClickNPick deliver the order as fast as you can to {delivery_address} within 7 working days for in case if the Order gets late contact the Customer or mail them at {customer_email} Payment method is Cash On Delivery'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["rahulagarwal24.ad@gmail.com", ]
            send_mail( subject, message, email_from, recipient_list )

            #Mail thing
            subject = 'Thank you for Ordering in JC&P'
            message = f'Hi {customer_firstName}, thank you for Ordering {product_name}({product_quantity}) of Amount Rs {total_price} from JustClickNPick your Order will be delivered at {delivery_address} within 7 working days for in case if the Order gets late contact us on www.justclicknpick.in/contact or mail us on {settings.EMAIL_HOST_USER} Payment method is Cash On Delivery'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [customer_email, ]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'Your order has been placed successfully')
            return redirect('home')
        except Exception as e:
            messages.success(request,'Your order has been placed successfully')
            return redirect('home')

    product = Product.objects.filter(product_id = id,instock__gte = 1)
    if not request.user.is_authenticated:
        messages.error(request,'Please log in to proceed further')
    if len(product) > 0:
        return render(request,'shop/checkout.html',{"product":product})
    return httpresponse("404 error")

def product(request,id):
    product = Product.objects.filter(product_id=id,instock__gte = 1)
    if not product:
        return httpresponse("404 Error")
    comments = ProductComment.objects.filter(product = product[0])
    from datetime import datetime as DateTime, timedelta as TimeDelta, date
    date_1 = date.today()
    end_date = date_1 + TimeDelta(days=7)
    end_date = end_date.strftime("%A, %B %d, %Y")
    query = product[0].category
    query = query.lower()
    allprods = Product.objects.all()
    products = searchTheProductforShow(query.lower(),allprods)
    params = {'product':product,'products':products,'comments':comments,'user':request.user,'delivery_date':end_date}
    return render(request,'shop/product.html',params)

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
            try:
                subject = 'welcome to JC&P world'
                message = f'Hi {myuser.first_name}, thank you for registering in JustClickNPick your register id is {myuser.email} and Password is {password1}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [myuser.email, ]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request,'Your Acount has been Registered')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception as f:
                messages.success(request,'Your Acount has been Registered')
                return redirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            print(e)
            messages.error(request,'server error occur try again after some time')
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER'))
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
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return httpresponse('404 - not found')

def handleLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Successfully logged out')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return httpresponse('404 error')

def order(request):
    if request.user.is_authenticated:
        orders = reversed(Order.objects.filter(customer_username=request.user.username))
        return render(request,'shop/order.html',{"orders":orders})
    else:
        messages.warning(request,'please log in first to see your orders')
        return render(request,'shop/order.html')

def productComment(request):
    if request.method=="POST":
        comments = request.POST.get("comment")
        user = request.user
        product_id = request.POST.get("product_id")
        product = Product.objects.get(product_id=product_id)
        comment = ProductComment(comments=comments,user=user,product=product)
        comment.save()
        messages.success(request,"Your comment has been posted succesfully")
    return redirect(request.META.get('HTTP_REFERER'))
        