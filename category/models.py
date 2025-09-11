from django.db import models
from common.models import BaseModel
# Create your models here.

# Model for product categories
class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_image/%Y/%m/%d/', blank=True, null=True)
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
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]
