from django import forms
from .models import Wishlist, Book

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['books']
