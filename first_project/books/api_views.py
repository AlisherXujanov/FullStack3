from django.forms import model_to_dict
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .usecases import *
from .models import Books, Genre
from .serializers import BooksSerializer, GenreSerializer
from django.shortcuts import get_object_or_404
from first_project.throttles import TenMinuteThrottle
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

class BooksViewSet(AuthApiView):
    throttle_classes = [TenMinuteThrottle]

    @method_decorator(cache_page(SHORT_CACHING_TIME))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, request):
        all_books = Books.objects.all()

        genre = request.query_params.get('genre')
        author = request.query_params.get('author')
        order = request.query_params.get('order')
        order_desc = request.query_params.get('order-desc')

        # "/books/?order-desc=price&genre=horror&author=John"

        if genre:
            all_books = all_books.filter(genre__slug=genre.strip())
        if author:
            all_books = all_books.filter(author__username=author)
        
        if order:
            all_books = all_books.order_by(order)
        elif order_desc:
            all_books = all_books.order_by(f'-{order_desc}')

        books = BooksSerializer(all_books, many=True, context={'request': request})
        return Response(books.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = BooksSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)

class GenreDetails(AuthApiView):
    def get(self, request, slug):
        genre = get_object_or_404(Genre, slug=slug)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


"""
# @api_view(["GET"])
# def books_list(request):
#     return Response({"Hello": "World"}, status=status.HTTP_200_OK)

# class BooksViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
#     permission_classes = [permissions.IsAuthenticated]

# {
#   "title": "Test title",
#   "genre": "Test genre", 
#   "description": "test desc", 
#   "price": 20
# }
"""

