import json
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from book.models import Book
from review.models import *

# Create your views here.
def get_reviews_json(request):
    reviews = Review.objects.all()
    return HttpResponse(serializers.serialize("json", reviews), content_type="application/json")

def show_reviews(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'show_reviews.html', context)

def show_reviews_by_book_id(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    book_rating = BookRating.objects.filter(book=book)

    context = {
        'book': book,
        'reviews': reviews,
        'book_rating': book_rating,
    }

    return render(request, 'show_reviews_by_book_id', context)

@csrf_exempt
def create_review_ajax(request, book_id):
    if request.method == 'POST':
        user = request.user
        book = get_object_or_404(Book, pk=book_id)
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        new_review = Review(user=user, book=book, rating=rating, comment=comment)

        try:
            new_review.full_clean()
        except ValidationError as e:
            return HttpResponse(str(e), status=400)

        new_review.save()

        book_rating, created = BookRating.objects.get_or_create(book=book)
        if not created:
            total_reviews = Review.objects.filter(book=book).count()
            total_ratings = sum([review.rating for review in Review.objects.filter(book=book)])
            book_rating.rating = total_ratings / total_reviews
        else:
            book_rating.rating = new_review.rating

        book_rating.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_review_ajax(request, review_id):
    if request.method == 'DELETE':
        review = get_object_or_404(Review, pk=review_id)

        if request.user == review.user:
            book = review.book

            review.delete()

            book_rating = BookRating.objects.get(book=book)
            total_reviews = Review.objects.filter(book=book).count()
            if total_reviews > 0:
                total_ratings = sum([review.rating for review in Review.objects.filter(book=book)])
                book_rating.rating = total_ratings / total_reviews
            else:
                book_rating.rating = 0
            book_rating.save()

            return HttpResponse("OK", status=204)
        else:
            return HttpResponse("Unauthorized", status=401) 
    return HttpResponseNotFound()

@csrf_exempt
def update_review_ajax(request, review_id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        new_rating = data.get('rating')
        new_comment = data.get('comment')

        review = get_object_or_404(Review, pk=review_id)
        book = review.book

        if request.user == review.user:
            if new_rating is not None:
                review.rating = new_rating

                book_rating = BookRating.objects.get(book=book)
                total_reviews = Review.objects.filter(book=book).count()
                total_ratings = sum([review.rating for review in Review.objects.filter(book=book)])
                book_rating.rating = total_ratings / total_reviews
                book_rating.save()

            if new_comment is not None:
                review.comment = new_comment

            review.save()

            return HttpResponse("OK", status=200)
        else:
            return HttpResponse("Unauthorized", status=401)
    return HttpResponseNotFound()