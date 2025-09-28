from django.contrib import admin

# Register your models here.
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'trending', 'created_at','image')
    list_editable = ('status', 'name', 'trending')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_per_page = 10
admin.site.register(Category, CategoryAdmin)  