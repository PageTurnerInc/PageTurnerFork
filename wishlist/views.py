from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Wishlist
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import datetime

@login_required(login_url='/login')
def show_main(request):
    # Ambil semua buku yang tersedia
    available_books = Book.objects.all()

    context = {
        'books': available_books,
    }

    return render(request, 'main.html', context)

@login_required(login_url='/login')
def show_wishlist(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    books = [wishlist.books for wishlist in wishlists]

    context = {
        'wishlist': books,  # Mengirim daftar buku ke template
        'user': user
    }
    return render(request, 'wishlist.html', context)

@login_required(login_url='/login')
def add_to_wishlist(request, book_id):
    if request.method == "GET":
        return HttpResponseRedirect(reverse("wishlist:show_main"))
    if request.method == "POST":
        books = Book.objects.get(id=book_id)
        try:
            wish_book = Wishlist.objects.get(user=request.user, books=books)
            if wish_book:
                wish_book.save()
        except Wishlist.DoesNotExist:
            Wishlist.objects.create(user=request.user, books=books)
        return HttpResponseRedirect(reverse("wishlist:show_wishlist"))
        

        
# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been successfully created!')
#             return redirect('wishlist:login')
#     context = {'form':form}
#     return render(request, 'register.html', context)

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             response = HttpResponseRedirect(reverse("wishlist:show_main")) 
#             response.set_cookie('last_login', str(datetime.datetime.now()))
#             return response
#         else:
#             messages.info(request, 'Sorry, incorrect username or password. Please try again.')
#     context = {}
#     return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('wishlist:login'))
#     response.delete_cookie('last_login')
#     return response

@login_required(login_url='/login')
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