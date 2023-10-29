from django.contrib import admin

from review.models import BookRating, Review

# Register your models here.
admin.site.register(BookRating)
admin.site.register(Review)