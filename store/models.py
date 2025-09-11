from django.db import models
from django.test import tag
from category.models import Category 
from common.models import BaseModel
# Create your models here.

# Model for product
class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    product_image = models.ImageField(upload_to='product_image/%Y/%m/%d/', blank=True, null=True)
    small_description = models.CharField(max_length=250, blank=True, null=True)
    quantity = models.IntegerField(null=False, blank=False,default=0)
    original_price = models.FloatField(null=False, blank=False,default=0.0)
    selling_price = models.FloatField(null=False, blank=False,default=0.0)
    tags = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, max_length=500,null=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.TextField(max_length=500, blank=True, null=True)
   



    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]
