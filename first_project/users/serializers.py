from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer, 
    TokenRefreshSerializer
)
from typing import Any, Dict
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from users.models import Profile
from rest_framework import exceptions
from .usecases import *


class BFTokenObtainPairSerializer(TokenObtainPairSerializer):
    NO_ACTIVE_ACCOUNT = f"Who are you?   You have no account!   Bye Bye! 😭"


    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        """
            TokenObtainPairSerializer allows us to pass only username (no email) to validation
            But in the username_field we also can pass Email and if it is not correct AuthenticationFailed raised
            else: by Email up is retrieved and with up.user.username another attrs is created for original validation
        """
        if up := Profile.objects.filter(user__username=attrs.get('username')).first():
            attrs = {
                'username': up.user.username, 
                'password':attrs['password']
            }
            if can_login_again(up):
                try:
                    super(BFTokenObtainPairSerializer, self).validate(attrs)
                    successful_login_attempt(up)
                except exceptions.AuthenticationFailed:
                    failed_login_attempt(up)
                    raise exceptions.AuthenticationFailed(
                        self.NO_ACTIVE_ACCOUNT,
                        'no_active_account',
                    )
            else:
                seconds_to_wait = (next_login_allowed_time(up) - timezone.now()).seconds
                raise exceptions.AuthenticationFailed(
                    f'You have been delayed for next login. Please try again later! ' + str(seconds_to_wait) + " seconds left!", 
                    'login_delayed'
                )
        else:
            raise exceptions.AuthenticationFailed(
                self.NO_ACTIVE_ACCOUNT, 
                'no_active_account'
            )
        
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data

class BFTokenRefreshSerializer(TokenRefreshSerializer):
    pass