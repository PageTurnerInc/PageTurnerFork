from django.db import models
from main.models import Account
from book.models import Book
from django.forms import ModelForm

# Create your models here.
class Rak(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE) 
    books = models.ManyToManyField(Book)

class RakForm(ModelForm):
    class Meta:
        model = Rak
        fields = ["name", "description"]