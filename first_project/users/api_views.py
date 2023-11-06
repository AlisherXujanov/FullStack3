from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import (
    BFTokenObtainPairSerializer,
    BFTokenRefreshSerializer
)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    else:
        return Response({'error': 'Wrong credentials'}, status=400)



class BFTokenObtainPairView(TokenObtainPairView):
    serializer_class = BFTokenObtainPairSerializer

class BFTokenRefreshView(TokenRefreshView):
    serializer_class = BFTokenRefreshSerializer