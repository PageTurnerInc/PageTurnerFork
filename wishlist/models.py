from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     cover_image = models.ImageField(upload_to='book_covers/')
#     synopsis = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)

