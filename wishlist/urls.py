from django.urls import path
from wishlist.views import add_to_wishlist, login_user, show_wishlist, show_main, register, logout_user, delete_book

app_name = 'wishlist'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('wishlist/', show_wishlist, name='show_wishlist'),
    path('add_to_wishlist/<int:book_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    
]
