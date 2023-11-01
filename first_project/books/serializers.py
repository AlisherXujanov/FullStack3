from unicodedata import lookup
from .models import Books, Genre
from rest_framework import serializers


DISCOUNT_IN_PERCENT = 10


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Genre
        fields = ["name", "slug"]



class BooksSerializer(serializers.ModelSerializer):
    price_in_discount = serializers.SerializerMethodField(
                                            method_name='get_price_in_discount')
    name = serializers.CharField(source='title')
    genre = serializers.HyperlinkedRelatedField(
        queryset=Genre.objects.all(),
        view_name='genre-detail',
        lookup_field='slug'
    )
    # genre = GenreSerializer()

    class Meta:
        model = Books
        fields = ["name", "genre", "description", "price_in_discount"]

    def get_price_in_discount(self, obj:Books):
        price = obj.price - (obj.price * DISCOUNT_IN_PERCENT / 100) 
        return f'${price} ({DISCOUNT_IN_PERCENT}% discount)'
