from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product


# ==========================================================
# Store Views
# ==========================================================
# These views handle:
# 1) Home page
# 2) Category listing and category product listing
# 3) Product detail page


def home(request):
    """Display the main store homepage."""
    return render(request, 'store/index.html')




def category_list(request):
    """Display all active categories.

    A category is considered active when `status=0`.
    """
    categories = Category.objects.filter(status=0)
    context = {
        'categories': categories
    }
    return render(request, 'store/category_list.html', context)





# ----------------------------------------------------------
# Category detail view (shows products in one category)
# ----------------------------------------------------------
def category_detail(request, slug):
    """Display products for a single active category by slug.

    Returns 404 automatically if the category does not exist
    or is not active.
    """
    category = get_object_or_404(Category, slug=slug, status=0)
    products = Product.objects.filter(category=category)

    context = {
        'products': products,
        'category': category
    }
    return render(request, 'store/category_detail.html', context)    


# ----------------------------------------------------------
# Product detail view
# ----------------------------------------------------------
def product_detail(request, cate_slug, prod_slug):
    """Display one active product in a given category.

    Looks up the product by both category slug and product slug,
    then returns 404 if no matching active product is found.
    """
    product = get_object_or_404(Product, category__slug=cate_slug, slug=prod_slug, status=False)
    context = {
        'product': product
    }
    return render(request, 'store/product_detail.html', context)
