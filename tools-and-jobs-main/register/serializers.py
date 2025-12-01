from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Company
# adjust import path if your job model is elsewhere
from jobs.models import add_jobs  

class CompanyRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    company_email = serializers.EmailField(required=False)

    class Meta:
        model = Company
        fields = [
            'username', 'password',
            'company_name', 'company_email', 'company_phone',
            'company_address', 'is_company_verified'
        ]

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        company_email = validated_data.get('company_email', '')

        # Create the Django user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=company_email or ''
        )

        user.is_active = True
        user.is_staff = True       # <-- REQUIRED for admin login
        user.save()

        # Add to company-admin group
        group, _ = Group.objects.get_or_create(name="CompanyAdmins")
        try:
            ct = ContentType.objects.get_for_model(add_jobs)
            perms = Permission.objects.filter(
                content_type=ct,
                codename__in=[
                    f"add_{add_jobs._meta.model_name}",
                    f"change_{add_jobs._meta.model_name}",
                    f"delete_{add_jobs._meta.model_name}",
                ]
            )
            # idempotent: add the perms (won't duplicate)
            group.permissions.add(*perms)
        except Exception:
            # if the jobs model is not importable in this context, don't crash.
            # you can ensure group perms via a migration or shell later.
            pass

        # 3) add the user to the group
        user.groups.add(group)

        # 4) create the Company record linked to this user
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
