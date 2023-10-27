from django.forms import ModelForm
from rak_buku.models import Rak

class RakForm(ModelForm):
    class Meta:
        model = Rak
        fields = ["name", "description"]