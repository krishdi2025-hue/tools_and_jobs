from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

    def validate(self, attrs):
        # change "username" to "email"
        credentials = {
            'email': attrs.get("email"),
            'password': attrs.get("password")
        }
        return super().validate(credentials)
