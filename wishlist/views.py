import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Wishlist, Notes
from main.models import Account  
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .forms import WishlistForm


@login_required(login_url='main:login_user')
def show_wishlist(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    books = [wishlist.books for wishlist in wishlists]
    context = {
        'books': books,  
        'user': user,
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
    

    try:
        wishlist_item = Wishlist.objects.get(user=request.user, books=book)
        wishlist_item.delete()
    except Wishlist.DoesNotExist:
        pass

    return HttpResponseRedirect(reverse("wishlist:show_wishlist"))

def get_wishlist_items(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)
    wishlist_items = []
    for wishlist in wishlists:
        book = wishlist.books
        item = {
            'image_url_l': book.image_url_l,
            'book_title': book.book_title,
            'book_author': book.book_author,
            'year_of_publication': book.year_of_publication,
            'publisher': book.publisher,
            'pk' : book.pk ,
        }
        wishlist_items.append(item)
    return HttpResponse(json.dumps(wishlist_items), content_type="application/json")

def add_notes(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        notes = request.POST.get("notes")
        user = request.user
        new = Notes(title=title,notes=notes,user=user)
        new.save()
    return HttpResponseRedirect(reverse("wishlist:show_notes"))

def show_notes(request):
    user = request.user
    notes = Notes.objects.filter(user=user)

    context = {
        'notes': notes, 
        'user': user,
    }
    return render(request, 'notes.html', context)



def get_notes(request):
    notes = Notes.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', notes))

@csrf_exempt
def add_notes_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_note = Notes.objects.create(
            user = request.user,
            title = data["title"],
            notes = data["notes"]
        )

        new_note.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt 
def delete_book_flutter(request, book_id):
    if request.method == 'DELETE':
        book = get_object_or_404(Book, id=book_id)

        try:
            wishlist_item = Wishlist.objects.get(user=request.user, books=book)
            wishlist_item.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Wishlist.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Book not found in wishlist"}, status=404)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
