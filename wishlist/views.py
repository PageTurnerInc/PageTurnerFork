from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Wishlist
from main.models import Account  # Impor model Account dari modul "main"
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='main:login_user')
def show_main(request):
    # Ambil semua buku yang tersedia
    available_books = Book.objects.all()

    context = {
        'books': available_books,
    }

    return render(request, 'main.html', context)

@login_required(login_url='main:login_user')
def show_wishlist(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    books = [wishlist.books for wishlist in wishlists]

    context = {
        'books': books,  # Mengirim daftar buku ke template
        'user': user
    }
    return render(request, 'wishlist.html', context)

@login_required(login_url='main:login_user')
def add_to_wishlist(request, book_id):
    # if request.method == "GET":
    #     return HttpResponseRedirect(reverse("wishlist:show_main"))
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
        messages.success(request, 'Book has been removed from your wishlist')
    except Wishlist.DoesNotExist:
        messages.error(request, 'Book not found in your wishlist')

    return HttpResponseRedirect(reverse("wishlist:show_wishlist"))

def get_wishlist_items(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    books = [wishlist.books for wishlist in wishlists]
    # Mengambil data yang sesuai dengan atribut yang Anda akses di JavaScript
    serialized_books = serializers.serialize('json', books, fields=('image_url_s', 'book_title', 'book_author', 'year_of_publication', 'publisher'))
    return HttpResponse(serialized_books, content_type="application/json")
