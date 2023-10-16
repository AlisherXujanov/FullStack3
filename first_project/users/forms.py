from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             help_text="We never share your email with anyone else.")

    class Meta:
        model = User
        fields = ('username', 'email',
                  'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', )
