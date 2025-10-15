from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import messages
from django.http import HttpResponse

# test
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

# test
def protected_view(request):
    jwt_auth = JWTAuthentication()
    try:
        user, token = jwt_auth.authenticate(request)
        return HttpResponse(f"Hello {user.username}")
    except AuthenticationFailed:
        return HttpResponse("Unauthorized", status=401)


def index_view(request):
    jwt_auth = JWTAuthentication()
    try:
        header = jwt_auth.get_header(request)
        if header is None:
            raise AuthenticationFailed("No token provided")

        raw_token = jwt_auth.get_raw_token(header)
        validated_token = jwt_auth.get_validated_token(raw_token)
        user = jwt_auth.get_user(validated_token)

        return render(request, "index.html", {"user": user})

    except Exception as e:
        messages.error(request, f"Authentication failed: {e}")
        return redirect("login")


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        # Try to fetch user by email
        try:
            user_obj = User.objects.get(email=Email)
            user = authenticate(request, username=user_obj.username, password=Password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            response = redirect("index")  # redirect to your dashboard page
            # Store tokens in cookies
            response.set_cookie("access", str(refresh.access_token), httponly=True)
            response.set_cookie("refresh", str(refresh), httponly=True)
            return response
        else:
            messages.error(request, "Invalid email or password")

    return render(request,'Login.html')


def logout_view(request):
    response = redirect("login")
    response.delete_cookie("access")
    response.delete_cookie("refresh")
    messages.success(request, "Logged out successfully!")
    return response
