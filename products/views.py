from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Product
from cart.forms import CartAddProductForm


def products_list(request, slug=None):
    category = None
    queryset = Product.available.all()


    if slug:
        category = get_object_or_404(Category, slug=slug)
        queryset = Product.available.filter(category=category)

    paginator = Paginator(queryset, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'categories': Category.objects.all(),
        'category': category,
        'product_list': page_obj
    }

    return render(request, 'products/product_list.html', data)

def product_detail(request, slug):
    produto = get_object_or_404(Product, slug=slug)
    if produto:
        data = {
            'product': produto,
            'form': CartAddProductForm()
        }
        return render(request, 'products/product_detail.html', data)
    
    redirect('products:product_list')
