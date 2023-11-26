from django.urls import path
from daftar_belanja.views import *

app_name = 'daftar_belanja'

urlpatterns = [
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('owned_books/', owned_books, name='owned_books'),
    path('get_cart_json/', get_cart_json, name='get_cart_json'),
    path('get_shopping_cart/', get_shopping_cart, name='get_shopping_cart'),
    path('get_owned_books/', get_owned_books, name='get_owned_books'),
    path('confirm_payment/', confirm_payment, name='confirm_payment'),
    path('check_book_ownership/', check_book_ownership, name='check_book_ownership'),
    path('add_to_cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('add_to_cart_ajax/', add_to_cart_ajax, name='add_to_cart_ajax'),
    path('remove_from_cart_ajax/', remove_from_cart_ajax, name='remove_from_cart_ajax'),
    path('delete_book_ajax/', delete_book_ajax, name='delete_book_ajax'),
]