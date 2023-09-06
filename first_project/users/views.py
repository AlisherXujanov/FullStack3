from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm
from .models import User


def first_view(request):
    context = {
        'form': UserForm(),
        "users": User.objects.all()
    }

    return render(request, 'index.html', context)
