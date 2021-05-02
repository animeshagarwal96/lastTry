from django.urls import path,include
from . import views

urlpatterns=[
    path("shop",views.index,name="shop"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("search",views.search,name="search"),
    path('orders',views.order,name="orders"),
    path("product/<int:id>",views.product,name="product"),
    path("checkout/<int:id>",views.checkout,name="checkout"),
    path('signup',views.handleSignup,name="signup"),
    path('login',views.handleLogin,name="login"),
    path('logout',views.handleLogout,name="logout"),
    path("",views.shop,name="home"),
    path("postcomment",views.productComment,name="comments")
]