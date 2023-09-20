from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
