import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from book.models import Book
from review.forms import ReviewForm
from review.models import *

# Create your views here.
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm(request.POST or None, initial={'book': book, 'user': request.user})

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.date = datetime.now()
            review.save()

            book_rating, created = BookRating.objects.get_or_create(book=book)
            print(book_rating)
            if not created:
                total_reviews = Review.objects.filter(book=book).count()
                total_ratings = float(sum([review.rating for review in Review.objects.filter(book=book)]))
                if total_reviews != 0:
                    book_rating.rating = total_ratings / total_reviews
                else:
                    book_rating.rating = float(review.rating)
            else:
                book_rating.rating = review.rating

            book_rating.save()

            return HttpResponseRedirect(reverse('review:show_reviews_by_book_id', args=(book_id,)))

    context = {'form': form, 'name': request.user.username}
    return render(request, "make_review.html", context)

def get_book_rating_by_book_id(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    rating = BookRating.objects.filter(book=book)
    return HttpResponse(serializers.serialize("json", rating), content_type="application/json")

def get_reviews_json(request):
    reviews = Review.objects.all()
    return HttpResponse(serializers.serialize("json", reviews), content_type="application/json")

def get_others_reviews_json(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book).exclude(user=user)
    return HttpResponse(serializers.serialize("json", reviews), content_type="application/json")

def get_reviews_json_by_book_id(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book).order_by('-date')
    return HttpResponse(serializers.serialize("json", reviews), content_type="application/json")

def get_reviews_json_by_request_id(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(user=user, book=book)
    return HttpResponse(serializers.serialize("json", reviews), content_type="application/json")

def show_reviews_by_book_id(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book).order_by('-date')
    book_rating = BookRating.objects.filter(book=book)
    # print(book_rating.fields.rating)
    context = {
        'book': book,
        'reviews': reviews,
        'book_rating': book_rating,
    }

    return render(request, 'show_reviews_by_book_id.html', context)

@csrf_exempt
def create_review_ajax(request, book_id):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST.get("rating"))
        user = request.user
        book = get_object_or_404(Book, pk=book_id)
        data = json.loads(request.body)
        rating = int(data.get('rating'))
        comment = data.get('comment')
        reviewer = request.user.username
        date = datetime.now()

        if comment == "":
            comment = ""

        new_review = Review(user=user, book=book, reviewer=reviewer, rating=rating, comment=comment, date=date)

        try:
            new_review.full_clean()
        except ValidationError as e:
            return HttpResponse(str(e), status=400)

        new_review.save()

        book_rating, created = BookRating.objects.get_or_create(book=book)
        print(book_rating)
        if not created:
            total_reviews = Review.objects.filter(book=book).count()
            total_ratings = float(sum([review.rating for review in Review.objects.filter(book=book)]))
            if total_reviews != 0:
                book_rating.rating = total_ratings / total_reviews
            else:
                book_rating.rating = float(new_review.rating)
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
        print(data)
        new_rating = data.get('rating')
        new_comment = data.get('comment')

        review = get_object_or_404(Review, pk=review_id)
        book = review.book

        print(book)
        if request.user == review.user:
            if new_rating is not None:
                review.rating = int(new_rating)
                review.date = datetime.now()
                review.save()

                book_rating = BookRating.objects.get(book=book)
                total_reviews = Review.objects.filter(book=book).count()
                total_ratings = sum([review.rating for review in Review.objects.filter(book=book)])
                book_rating.rating = total_ratings / total_reviews

                if total_reviews != 0:
                    book_rating.rating = total_ratings / total_reviews
                else:
                    book_rating.rating = 0  # Set a default value if there are no reviews
                book_rating.save()

            if new_comment != '':
                review.comment = new_comment
                review.save()

            return HttpResponse("OK", status=200)
        else:
            return HttpResponse("Unauthorized", status=401)
    return HttpResponseNotFound()