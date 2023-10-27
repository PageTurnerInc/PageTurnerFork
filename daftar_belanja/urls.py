from django.urls import path
from daftar_belanja.views import *

app_name = 'daftar_belanja'

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('buy_book/<int:book_id>', buy_book, name='buy_book'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
]