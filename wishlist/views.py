from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Wishlist
from main.models import Account  
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='main:login_user')
def show_wishlist(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    books = [wishlist.books for wishlist in wishlists]

    context = {
        'books': books,  
        'user': user
    }
    return render(request, 'wishlist.html', context)

@login_required(login_url='main:login_user')
def add_to_wishlist(request, book_id):
    user = request.user

    try:
        account = Account.objects.get(user=user)
        is_premium = account.get_is_premium()
        if not is_premium:
            return HttpResponse("Anda harus menjadi pengguna premium untuk menambahkan item ke wishlist.")
    except Account.DoesNotExist:
        pass
    if request.method == "POST":
        books = Book.objects.get(id=book_id)
        try:
            wish_book = Wishlist.objects.get(user=request.user, books=books)
            if wish_book:
                wish_book.save()
        except Wishlist.DoesNotExist:
            Wishlist.objects.create(user=request.user, books=books)
        return HttpResponseRedirect(reverse("wishlist:show_wishlist"))

@csrf_exempt 
@login_required(login_url='main:login_user')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Pastikan bahwa item wishlist ini dimiliki oleh pengguna yang sedang masuk
    try:
        wishlist_item = Wishlist.objects.get(user=request.user, books=book)
        wishlist_item.delete()
    except Wishlist.DoesNotExist:
        pass

    return HttpResponseRedirect(reverse("wishlist:show_wishlist"))

def get_wishlist_items(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    books = [wishlist.books for wishlist in wishlists]
    return HttpResponse(serializers.serialize('json', books, fields=('image_url_l', 'book_title', 'book_author', 'year_of_publication', 'publisher')), content_type="application/json")
