from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateAccountForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)

    ACCOUNT_TIER = [('Y', 'Yes'), ('N', 'No')]
    is_premium = forms.ChoiceField(
        label="Would you like to sign up for a premium account?",
        required=True,
        choices=ACCOUNT_TIER,
    )

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'is_premium', 'password1']

    def save(self, commit=True):
        user = super(CreateAccountForm, self).save(commit=False)
        user.full_name = self.cleaned_data["full_name"]
        user.email = self.cleaned_data["email"]
        user.is_premium = self.cleaned_data["is_premium"]

        if commit: 
            user.save()

        return user