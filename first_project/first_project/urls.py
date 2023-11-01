"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from .views import *

from rest_framework import routers
from books.api_views import *

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-rest/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += i18n_patterns(
     # Patterns that need to be translated
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
    path("", HomeView.as_view(), name="home_page"),
    path("wishlist/", wishlist_view, name="wishlist_view"),
    path("send_email/", send_email_view, name="send_email_view"),
    path("delete_from_wl/<int:book_id>/",
         delete_from_wl, name="delete_from_wl"),
    path('accounts/', include('allauth.urls')),
    path('translate/<str:language>/', translate, name="translate"),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
