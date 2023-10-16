from django import forms
from django.contrib.auth.models import User


class SendEmailForm(forms.Form):
    title = forms.CharField(max_length=50)
    message = forms.CharField(max_length=255)
    email = forms.EmailField()

