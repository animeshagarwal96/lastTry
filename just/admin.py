from django.contrib import admin
from .models import Product,Users,Contact,Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Users)
admin.site.register(Contact)
admin.site.register(Order)

admin.site.site_header = "JustClickNPick"
admin.site.site_title = "JustClicNPick Admin"
admin.site.index_title = "Welcome to JCNP Admin"
