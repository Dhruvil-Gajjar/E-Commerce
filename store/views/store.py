from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from store.utils import *


def store(request):
    data = cartData(request)

    cartItems = data['cartItems']

    products = Product.objects.all()

    # Pagination
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def product_detail(request):

    # data = cartData(request)
    # cartItems = data['cartItems']
    # users = Customer.objects.filter(user=request.user)
    #
    # context = {'users': users, 'cartItems': cartItems}
    return render(request, 'store/product-detail.html')

