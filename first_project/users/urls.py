from django.urls import path

from .views import first_view

urlpatterns = [
    path("", first_view, name="first_view")
]
