from django.forms import model_to_dict
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .usecases import *
from .models import Books
from .serializers import BooksSerializer


# @api_view(["GET"])
# def books_list(request):
#     return Response({"Hello": "World"}, status=status.HTTP_200_OK)

class BooksList(AuthApiView):
    def get(self, request):
        all_books = Books.objects.all()
        books = BooksSerializer(all_books, many=True)
        return Response(books.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print(data)




class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]
