from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name="landing"),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('create_account/', create_account, name='create_account'),
]