from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm
from .models import User


def first_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    context = {
        'form': UserForm(),
        "users": User.objects.all()
    }

    return render(request, 'index.html', context)