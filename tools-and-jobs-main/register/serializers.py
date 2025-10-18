from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class CompanyRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    company_email = serializers.EmailField(required=False)

    class Meta:
        model = Company
        fields = ['username', 'password', 'company_name', 'company_email', 'company_phone', 'company_address']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        # Extract company email if provided and set it on the Django user
        company_email = validated_data.get('company_email')
        user = User.objects.create_user(username=username, password=password, email=company_email or '')
        company = Company.objects.create(user=user, **validated_data)
        return company

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('A user with that username already exists.')
        return value

    def validate_company_email(self, value):
        # If you want company emails to be unique across users, uncomment below
        # if User.objects.filter(email__iexact=value).exists():
        #     raise serializers.ValidationError('A user with that email already exists.')
        return value