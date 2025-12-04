from django.urls import path
from .views import contacto_view, add_to_cart_view, remove_from_cart_view, clear_cart_view

app_name = 'contacto'

urlpatterns = [
    path('', contacto_view, name='contacto'),
    path('cart/add/<str:item_type>/<int:item_id>/', add_to_cart_view, name='add_to_cart'),
    path('cart/remove/<str:item_type>/<int:item_id>/', remove_from_cart_view, name='remove_from_cart'),
    path('cart/clear/', clear_cart_view, name='clear_cart'),
]
