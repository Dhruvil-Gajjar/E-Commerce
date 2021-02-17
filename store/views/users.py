import datetime

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from store.utils import *
from store.forms import UserEditForm


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print('Action:', action)
    # print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)


def myaccount_view(request):
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
        users = Customer.objects.filter(user=request.user)

        context = {'users': users, 'cartItems': cartItems}
        return render(request, 'store/my-account.html', context)

    else:
        return redirect('/')


def myorder_view(request):
    orders = Order.objects.all()
    if request.GET.get('users_id', ''):
        customers = Customer.objects.get(id=request.GET.get('users_id'))
        orders = customers.users.all()
    return render(request, "store/my-orders.html", {'orders': orders})


def userEdit_view(request):
    if request.method == 'POST':
        user_edit = UserEditForm(request.POST, instance=request.user)
        if user_edit.is_valid():
            user_edit.save()

            messages.success(request, 'Your Profile has been updated!')
            return redirect('/my_account')
    else:
        user_edit = UserEditForm(instance=request.user)

    context = {'user_edit': user_edit}
    return render(request, 'store/user-edit.html', context)
