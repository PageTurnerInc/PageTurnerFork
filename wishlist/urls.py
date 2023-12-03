from django.urls import path
from wishlist.views import add_notes_flutter, add_to_wishlist, add_to_wishlist_flutter, delete_book_flutter,  show_wishlist,  delete_book, get_wishlist_items, add_notes, show_notes,get_notes

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('add_to_wishlist/<int:book_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('get_wishlist_items/', get_wishlist_items, name='get_wishlist_items'),
    path('add_notes/', add_notes, name='add_notes'),
    path('show_notes/', show_notes, name='show_notes'),
    path('get_notes/', get_notes, name='get_notes'),
    path('add_notes_flutter/', add_notes_flutter, name='add_notes_flutter'),
    path('delete_book_flutter/<int:book_id>/', delete_book_flutter, name='delete_book_flutter'),
    path('add_to_wishlist_flutter/', add_to_wishlist_flutter, name='add_to_wishlist_flutter'),


    
]
