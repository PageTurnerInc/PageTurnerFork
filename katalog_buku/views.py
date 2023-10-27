from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

from book.models import Book
from rak_buku.models import Rak
from main.models import Account


def show_katalog(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    
    return render(request, "katalog_buku.html", context)

def show_book_page(request, id):
    book = Book.objects.get(pk=id)
    user = Account.objects.get(user=request.user)
    user_rak = Rak.objects.filter(user=user)
    
    delete = False
    if request.user == book.user:
        delete = True

    context = {
        'book': book,
        'delete': delete,
        'user_rak': user_rak,
    }

    return render(request, "book_page.html", context)

@csrf_exempt
def add_book_katalog(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")
        book_title = request.POST.get("title")
        book_author = request.POST.get("author")
        year_of_publication = request.POST.get("year")
        publisher = request.POST.get("publisher")
        user = request.user
        print(isbn, book_title, book_author, year_of_publication, publisher, user)

        new_book = Book(isbn=isbn, book_title=book_title, book_author=book_author, year_of_publication=year_of_publication, publisher=publisher, user=user)
        new_book.save()
        print("Buku berhasil dibuat")

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

def delete_book_katalog(request, id):
    book = Book.objects.get(pk=id)
    if request.user == book.user:
        book.delete()
        books = Book.objects.all()
        context = {
            'books': books 
        }
        return render(request, "katalog_buku.html", context)
    
    return redirect('katalog_buku:show_books')

def get_product_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))

def add_book_to_rak(request, id, rak_id):
    book = Book.objects.get(pk=id)
    rak = Rak.objects.get(pk=rak_id)
    rak.books.add(book)

    # Redirect to the show_book_page view
    return HttpResponse(b"CREATED", status=201)