from django.urls import path

from . import views

urlpatterns = [
    # Main
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    # User
    path('my_account/', views.myaccount_view, name='user_account'),
    path('edit_profile/', views.userEdit_view, name='edit_profile'),
    path('my_orders/', views.myorder_view, name='my_orders'),

    # Product
    path('product_detail/', views.product_detail, name='product_detail'),
]
