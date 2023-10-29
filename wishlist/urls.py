from django.urls import path
from wishlist.views import add_to_wishlist,  show_wishlist,  delete_book, get_wishlist_items, add_notes, show_notes,get_notes

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('add_to_wishlist/<int:book_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('get_wishlist_items/', get_wishlist_items, name='get_wishlist_items'),
    path('add_notes/', add_notes, name='add_notes'),
    path('show_notes/', show_notes, name='show_notes'),
    path('get_notes/', get_notes, name='get_notes'),
    
]
