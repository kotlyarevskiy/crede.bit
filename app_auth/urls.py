from django.urls import path
from .views import *

urlpatterns = [
    path('userpage',        user_page,      name = 'user_page'),
    path('login',           login_user,     name = 'login_user'),
    path('logout',          logout_user,    name = 'logout_user'),
    path('registration',    registration,   name = 'registration'),
]
