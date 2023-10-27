from django.db import models
from book.models import Book
from main.models import Account

# Create your models here.
class ShoppingCart(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Book)