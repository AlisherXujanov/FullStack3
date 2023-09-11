from django.urls import path

from .views import first_view, user_details

urlpatterns = [
    path("", first_view, name="first_view"),
    path("<int:user_id>", user_details, name="user_details")
]
