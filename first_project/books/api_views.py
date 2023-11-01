from django.forms import model_to_dict
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .usecases import *
from .models import Books, Genre
from .serializers import BooksSerializer, GenreSerializer
from django.shortcuts import get_object_or_404


class BooksViewSet(NoAuthApiView):
    def get(self, request):
        all_books = Books.objects.all()
        books = BooksSerializer(all_books, many=True, context={'request': request})
        return Response(books.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = BooksSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)

class GenreDetails(NoAuthApiView):
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
