from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product

# Create your views here.


#------Home----------------------------------------------
def home(request):
    return render(request, 'store/index.html')




#--------------Category listing  view----------------------------
def collection(request):
    category = Category.objects.filter(status=0)
    context = {
        'category':category
    }
    return render(request,'store/collections.html',context)





#--------------Category view----------------------------
# def collectionview(request, slug):
#     if Category.objects.filter(slug=slug, status=0).exists():
#         products = Product.objects.filter(category__slug=slug)
#         category_name = Category.objects.filter(slug=slug).first()
#         context = {
#             'products': products,
#             'category_name': category_name
#         }
#         return render(request, 'products/index.html', context)
#     else:
#         messages.warning(request, "No such category found")
#         return redirect('store:collection')

# Using get_object_or_404 for cleaner code
def collectionview(request, slug):
    category = get_object_or_404(Category, slug=slug, status=0)
    products = Product.objects.filter(category=category)

    context = {
        'products': products,
        'category_name': category
    }
    return render(request, 'products/index.html', context)    


#----------------Product detail view----------------------------

# def productview(request, cate_slug, prod_slug):
#     if Category.objects.filter(slug=cate_slug, status=0).exists():
#         if Product.objects.filter(slug=prod_slug, status=0).exists():
#             product = Product.objects.filter(slug=prod_slug, status=0).first()
#             context = {
#                 'product': product
#             }
#             return render(request, 'products/view.html', context)
#         else:
#             messages.error(request, "No such product found")
#             return redirect('store:collection')
#     else:
#         messages.error(request, "No such category found")
#         return redirect('store:collection')




#----Modified productview using get_object_or_404 for cleaner code
def productview(request, cate_slug, prod_slug):
    product = get_object_or_404(Product, category__slug=cate_slug, slug=prod_slug, status=False)
    context = {
        'product': product
    }
    return render(request, 'products/view.html', context)
