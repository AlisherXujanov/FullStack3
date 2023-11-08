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
from rest_framework.pagination import PageNumberPagination


class BooksViewSet(AuthApiView):
    throttle_classes = [TenMinuteThrottle]

    def get(self, request):
        all_books = Books.objects.all()
        paginator = PageNumberPagination()

        genre = request.query_params.get('genre')
        author = request.query_params.get('author')
        order = request.query_params.get('order')
        order_desc = request.query_params.get('order-desc')

        # ex:  "/books/?order-desc=price&genre=...&author=..."

        if genre:
            all_books = all_books.filter(genre__slug=genre.strip())
        if author:
            all_books = all_books.filter(author__username=author)
        
        if order:
            all_books = all_books.order_by(order)
        elif order_desc:
            all_books = all_books.order_by(f'-{order_desc}')

        result_page = paginator.paginate_queryset(all_books, request)
        books = BooksSerializer(result_page, many=True, 
                                context={'request': request})
        return paginator.get_paginated_response(books.data)

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

