from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as django_login
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        email = request.POST.get('company_email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        company_name = request.POST.get('company_name')
        company_phone = request.POST.get('company_phone')
        company_address = request.POST.get('company_address')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "register.html")

        user = User.objects.create_user(
            email=email,
            password=password,
            company_name=company_name,
            company_phone=company_phone,
            company_address=company_address
        )
        user.save()

        # Auto login + issue JWT
        django_login(request, user)
        refresh = RefreshToken.for_user(user)
        response = redirect('/')
        response.set_cookie('access_token', str(refresh.access_token), httponly=True, max_age=60*15, samesite='Lax')
        response.set_cookie('refresh_token', str(refresh), httponly=True, max_age=7*24*3600, samesite='Lax')
        return response

    return render(request, "register.html")
