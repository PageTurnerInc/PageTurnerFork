from main.models import Account
from book.models import Book
from daftar_belanja.models import ShoppingCart
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from main.forms import CreateAccountForm
from django.contrib.auth.decorators import login_required
import json

@login_required(login_url='/login')
def add_book(request):
    account = Account.objects.get(user=request.user)

    context = {
        'user': request.user.username,
        'account': account,
        'books': Book.objects.all(),
    }

    return render(request, 'add_book.html', context)

@login_required(login_url='/login')
def shopping_cart(request):
    account = Account.objects.get(user=request.user)
    cart, created = ShoppingCart.objects.get_or_create(account=account)

    context = {
        'user': request.user.username,
        'account': account,
        'cart': cart.cart.all,
    }

    return render(request, 'shopping_cart.html', context)

def buy_book(request, book_id):
    account = Account.objects.get(user=request.user)
    book = Book.objects.get(id=book_id)
    cart, created = ShoppingCart.objects.get_or_create(account=account)
    cart.cart.add(book)

    return redirect('daftar_belanja:add_book')