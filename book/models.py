from django.db import models
from isbn_field import ISBNField
<<<<<<< HEAD
=======
from django.contrib.auth.models import User
>>>>>>> c910354369d0a90573201f72a1a5bee7c30b8bd4

class Book(models.Model):
    isbn = ISBNField()
    book_title = models.TextField(null=True, blank=True)
    book_author = models.TextField(null=True, blank=True)
    year_of_publication = models.IntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_url_s = models.TextField(null=True, blank=True)
    image_url_m = models.TextField(null=True, blank=True)
    image_url_l = models.TextField(null=True, blank=True)
<<<<<<< HEAD
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
>>>>>>> c910354369d0a90573201f72a1a5bee7c30b8bd4
