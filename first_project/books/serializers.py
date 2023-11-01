from .models import Books
from rest_framework import serializers


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["title", "genre", "description", "price"]