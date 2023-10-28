from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from book.models import Book

# Create your models here.
class BookRating(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, primary_key=True)
    rating = models.FloatField(default=0.0)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.TextField()
    comment = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='unique_user_book')
        ]

    def clean(self):
        existing_reviews = Review.objects.filter(user=self.user, book=self.book)
        if self.pk:
            existing_reviews = existing_reviews.exclude(pk=self.pk)

        if existing_reviews.exists():
            raise ValidationError('User can only give one review for each book.')
