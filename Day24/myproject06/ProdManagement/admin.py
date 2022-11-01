from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ('Prodid', 'Prodname', 'Category', 'Prodtype', 'Price')