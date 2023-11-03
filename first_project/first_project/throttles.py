from rest_framework.throttling import UserRateThrottle



class TenMinuteThrottle(UserRateThrottle):
    scope = 'ten'