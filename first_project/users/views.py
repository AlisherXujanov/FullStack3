from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .usecases import *


def registration(request):
    form = UserCreationForm(request.POST)
    context = {'form': form}
    return render(request, 'create_user.html', context)
