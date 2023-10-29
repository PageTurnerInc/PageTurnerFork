from django import forms
from .models import Wishlist, Book, Notes

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['books']

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['notes']