from django.urls import path

from .views import *

urlpatterns = [
    path("", first_view, name="first_view"),
    path("details/<int:user_id>", user_details, name="user_details"),
    path("delete/<int:del_id>", delete_user, name="delete_user")
]
