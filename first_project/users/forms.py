from django import forms

from .models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = '__all__'
