from django.urls import path
from review.views import *

app_name = 'review'

urlpatterns = [
    path('', show_reviews, name='show_reviews'),
    path('reviews/<int:book_id>/', show_reviews_by_book_id, name='show_reviews_by_book_id'),
    path('reviews/json/', get_reviews_json, name='get_reviews_json'),
    path('reviews/create-review-ajax/<int:book_id>/', create_review_ajax, name="create_review_ajax"),
    path('reviews/delete-review-ajax/<int:review_id>/', delete_review_ajax, name="delete_review_ajax"),
    path('reviews/update-review-ajax/<int:review_id>/', update_review_ajax, name="update_review_ajax"),
]