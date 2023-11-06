from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer, 
    TokenRefreshSerializer
)
from typing import Any, Dict
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from users.models import Profile
from rest_framework import exceptions


class BFTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        """
            TokenObtainPairSerializer allows us to pass only username (no email) to validation
            But in the username_field we also can pass Email and if it is not correct AuthenticationFailed raised
            else: by Email up is retrieved and with up.user.username another attrs is created for original validation
        """
        if up := Profile.objects.filter(user__username=attrs[self.username_field]).first():
            attrs = {
                'username': up.user.username, 
                'password':attrs['password']
            }

            data = super().validate(attrs)

            refresh = self.get_token(self.user)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            if api_settings.UPDATE_LAST_LOGIN:
                update_last_login(None, self.user)

            return data
        else:
            raise exceptions.AuthenticationFailed(
                'Ты кто такой? Давай, до свидания!', 
                'no_active_account'
            )

class BFTokenRefreshSerializer(TokenRefreshSerializer):
    pass