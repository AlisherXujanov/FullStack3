from django import forms

from .models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=255, label="Your name",
        widget=forms.PasswordInput(attrs={'placeholder': 'Your name'})
    )
    last_name = forms.CharField(max_length=255, label="Your surname")
    email = forms.EmailField(required=True, label="Your email",
                             help_text="We will never share your information with anyone!")
    image = forms.ImageField(required=False, label="Your image")

    class Meta:
        model = User
        fields = '__all__'
