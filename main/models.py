from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    is_premium = models.CharField(max_length=3)

    def get_is_premium(self):
        if self.is_premium == "Yes":
            return True
        elif self.is_premium == "No":
            return False

    def __str__(self):
        return self.user.username
