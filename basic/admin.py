from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderMenu)