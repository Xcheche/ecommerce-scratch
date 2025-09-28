from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('collection/', views.collection, name='collection'),
    path('collection/<str:slug>/', views.collectionview, name='collectionview'),
    #----------------------Product Details----------------------
    path('collection/<str:cate_slug>/<str:prod_slug>/', views.productview, name='productview'),
    #----------------------Add to Cart----------------------

]