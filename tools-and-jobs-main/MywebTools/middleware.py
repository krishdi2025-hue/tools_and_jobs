# MywebTools/middleware.py
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser

class JWTAuthMiddleware(MiddlewareMixin):
    """
    Read 'access_token' from HttpOnly cookie and authenticate request.user
    so template views can use request.user and @login_required.
    """

    def process_request(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            request.user = getattr(request, 'user', AnonymousUser())
            return

        jwt_auth = JWTAuthentication()
        try:
            validated_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validated_token)
            request.user = user
            # also set .auth for compatibility
            request.auth = validated_token
        except Exception:
            request.user = getattr(request, 'user', AnonymousUser())
