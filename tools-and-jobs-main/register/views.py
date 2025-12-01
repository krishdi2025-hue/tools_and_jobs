from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as django_login
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Company

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        email = request.POST.get('company_email') or request.POST.get('company_email')  # ensure you use the right form name
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        company_name = request.POST.get('company_name')
        company_phone = request.POST.get('company_phone')
        company_address = request.POST.get('company_address')
        # checkbox gives 'on' when checked, None when not
        is_company_verified = request.POST.get('is_company_verified') == 'on'

        # basic validation
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "register.html")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Username already taken.")
            return render(request, "register.html")

        # create the user (don't pass is_company_verified here)
        user = User.objects.create_user(
            username=email,  # or whatever username you want
            email=email,
            password=password,
            # pass company_name/phone/address only if these are actual fields on your custom User.
            # From your earlier field list they are on User (company_name/company_phone/company_address) — if they are,
            # you can pass them here; otherwise leave them to be stored in Company.
        )

        # create the Company record related to the user and set is_company_verified there
        Company.objects.create(
            user=user,
            company_name=company_name,
            company_email=email,
            company_phone=company_phone,
            company_address=company_address,
            is_company_verified=is_company_verified
        )

        # auto-login + issue JWT
        django_login(request, user)
        refresh = RefreshToken.for_user(user)
        response = redirect('/')
        response.set_cookie('access_token', str(refresh.access_token), httponly=True, max_age=60*15, samesite='Lax')
        response.set_cookie('refresh_token', str(refresh), httponly=True, max_age=7*24*3600, samesite='Lax')
        return response

    return render(request, "register.html")

