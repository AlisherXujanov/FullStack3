from django.http import HttpResponse
from django.shortcuts import render


def first_view(request):
    return render(request, 'index.html')
