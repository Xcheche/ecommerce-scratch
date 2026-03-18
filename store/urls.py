from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    #----------------------Home----------------------
    path('', views.home, name='home'),
    #----------------------Category list----------------------
    path('categories/', views.category_list, name='category_list'),
    #----------------------Category detail----------------------
    path('categories/<str:slug>/', views.category_detail, name='category_detail'),
    #----------------------Product detail----------------------
    path('categories/<str:cate_slug>/<str:prod_slug>/', views.product_detail, name='product_detail'),
    #----------------------Add to Cart----------------------
]