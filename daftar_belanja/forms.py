from django.forms import ModelForm
from daftar_belanja.models import ShoppingCart

class PaymentForm(ModelForm):
    class Meta:
        model = ShoppingCart 
        fields = ["receiver", "payment"]