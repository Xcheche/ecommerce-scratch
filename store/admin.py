from django.contrib import admin
from .models import  Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'status')
    list_editable = ('quantity', 'status')
    search_fields = ('name', 'category__name')
    list_per_page = 10
    prepopulated_fields ={'slug': ('name',)}



  

admin.site.register(Product, ProductAdmin)

