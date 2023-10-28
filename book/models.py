from django.db import models
from isbn_field import ISBNField
from main.models import Account

class Book(models.Model):
    isbn = ISBNField()
    book_title = models.TextField(null=True, blank=True)
    book_author = models.TextField(null=True, blank=True)
    year_of_publication = models.IntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_url_s = models.TextField(null=True, blank=True)
    image_url_m = models.TextField(null=True, blank=True)
    image_url_l = models.TextField(null=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
