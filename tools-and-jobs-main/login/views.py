# login/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login as django_login, logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

@require_http_methods(["GET","POST"])
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, "Invalid email or password.")
            return render(request, "login/login.html")

        django_login(request, user)
        refresh = RefreshToken.for_user(user)
        response = redirect('/')
        response.set_cookie('access_token', str(refresh.access_token), httponly=True, max_age=60*15, samesite='Lax')
        response.set_cookie('refresh_token', str(refresh), httponly=True, max_age=7*24*3600, samesite='Lax')
        return response

    return render(request, "login.html")



def logout_view(request):
    response = redirect('login')
    # Remove cookies
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    django_logout(request)
    return response

@require_http_methods(["POST"])
def refresh_token_view(request):
    """
    Read refresh token from cookie, call simplejwt RefreshToken, set new access (and optionally refresh),
    rotate refresh tokens if ROTATE_REFRESH_TOKENS enabled.
    """
    refresh_token = request.COOKIES.get('refresh_token')
    if not refresh_token:
        return HttpResponse(status=401)

    try:
        refresh = RefreshToken(refresh_token)
        new_access = str(refresh.access_token)

        response = HttpResponse(status=200)
        response.set_cookie('access_token', new_access, httponly=True,
                            max_age=15*60, samesite='Lax', secure=False)
        # If ROTATE_REFRESH_TOKENS, you should set new refresh cookie after blacklisting old - handled if you create rotated token
        if hasattr(refresh, 'rotate'):
            # (Using simplejwt rotation automatically on token.refresh endpoint; here we are manual)
            new_refresh = str(refresh)
            response.set_cookie('refresh_token', new_refresh, httponly=True,
                                max_age=7*24*60*60, samesite='Lax', secure=False)

        return response
    except TokenError:
        return HttpResponse(status=401)
    




@login_required(login_url='login')
def dashboard_view(request):
    # request.user is already set by JWTAuthMiddleware
    return render(request, 'dashboard.html', {'user': request.user})
