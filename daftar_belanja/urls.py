from django.urls import path
from daftar_belanja.views import *

app_name = 'daftar_belanja'

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('owned_books/', owned_books, name='owned_books'),
    path('get_shopping_cart/', get_shopping_cart, name='get_shopping_cart'),
    path('get_owned_books/', get_owned_books, name='get_owned_books'),
    path('confirm_payment/', confirm_payment, name='confirm_payment'),
    path('check_book_ownership/', check_book_ownership, name='check_book_ownership'),
]