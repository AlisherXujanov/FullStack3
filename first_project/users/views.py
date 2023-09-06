from django.http import HttpResponse
from django.shortcuts import render

from .models import User


def first_view(request):
    context = {
        "users": User.objects.all()
    }

    return render(request, 'index.html', context)
