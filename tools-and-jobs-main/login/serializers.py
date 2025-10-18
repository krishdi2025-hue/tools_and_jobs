from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Allow login with either username or email.

    Accepts POST fields: 'username' (which can be email) and 'password'.
    If an email is provided, find the user with that email and substitute
    their username for authentication.
    """

    def validate(self, attrs):
        # Support both 'username' (default) and 'email' coming from frontend
        username_or_email = attrs.get('username') or attrs.get('email')
        password = attrs.get('password')

        if not username_or_email or not password:
            raise serializers.ValidationError('Username/email and password are required')

        # If input looks like an email, try to resolve a username
        user = None
        if '@' in username_or_email:
            user = User.objects.filter(email__iexact=username_or_email).first()

        if user:
            # call parent with the resolved username
            return super().validate({'username': user.username, 'password': password})

        # otherwise fall back to normal username authentication
        return super().validate(attrs)

    def __init__(self, *args, **kwargs):
        # Before DRF does field-level validation (which requires 'username'),
        # allow callers to pass 'email' and resolve it to the real username.
        data = kwargs.get('data')
        if data and 'email' in data and 'username' not in data:
            try:
                email = data.get('email')
                user = User.objects.filter(email__iexact=email).first()
                if user:
                    data = data.copy()
                    data['username'] = user.username
                    kwargs['data'] = data
            except Exception:
                # If DB access fails for any reason, fall back to original data
                pass

        super().__init__(*args, **kwargs)
