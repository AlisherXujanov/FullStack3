from django import forms
from django.contrib.auth.models import User

from .models import Books

author_choices = ((user.id, user.first_name) for user in User.objects.all())


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Book title",
                            help_text="Please enter book title")
    author = forms.CharField(max_length=255, label="Author", help_text="Please enter author name",
                             widget=forms.Select(choices=author_choices))
    review = forms.CharField(max_length=255, label="Review",
                             help_text="Please enter your review")
    genre = forms.CharField(max_length=255, label="Genre",
                            help_text="Please enter genre")
    price = forms.DecimalField(max_digits=5, decimal_places=2, label="Price",
                               help_text="Please enter price")
    image = forms.ImageField(required=False, label="Book image",
                             help_text="Please upload book image")

    class Meta:
        model = Books
        fields = '__all__'
