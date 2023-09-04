from django.http import HttpResponse
from django.shortcuts import render


def first_view(request):
    return HttpResponse("""
            <h1 style="color:red;">Hello, World!</h1>
            <b>Hello, World!</b>
        """)
