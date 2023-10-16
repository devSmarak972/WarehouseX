
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home),
    path('inventory/<int:id>', views.inventory),
    path('invoice/<int:id>', views.invoice),
    path('invoices', views.invoicelist),
    path('map', views.map),
    path('products', views.productgrid),
    path('product/<int:id>', views.productpage),
    path('cart', views.productslist),
    path('product/<int:id>/edit', views.editproduct),
    path('orders', views.orders),
    path('warehouses', views.warehouselist),
    path('login', views.login),
    path('register', views.register),
]
