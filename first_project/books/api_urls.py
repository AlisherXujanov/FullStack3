from django.urls import path
from .api_views import *

urlpatterns = [
    path('', BooksViewSet.as_view()),
    path('genre-detail/<slug:slug>/', GenreDetails.as_view(), name='genre-detail'),
]
