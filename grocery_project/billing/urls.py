from django.urls import path
from . import views

urlpatterns=[
    path('add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.view_cart,name='cart'),
    path('update/<int:product_id>/',views.update_cart,name='update_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('receipt/<int:sale_id>/',views.receipt,name='receipt'),
]
