from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CompanyRegisterSerializer
from django.contrib import messages
import requests
from django.db import IntegrityError


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['GET'])
@permission_classes([IsAdminUser])
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanyRegisterSerializer(companies, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def register_company(request):
    serializer = CompanyRegisterSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except IntegrityError:
            return Response({"error": "User with that username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Company registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register_company_page(request):
    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password'),
            'company_name': request.POST.get('company_name'),
            'company_email': request.POST.get('company_email'),
            'company_phone': request.POST.get('company_phone'),
            'company_address': request.POST.get('company_address'),
        }

        # Create the company directly instead of making an HTTP POST to the same server
        serializer = CompanyRegisterSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                messages.success(request, 'Registration successful! Please login.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Registration failed: username already exists.')
        else:
            messages.error(request, f"Registration failed: {serializer.errors}")

    return render(request, 'register.html')


def company_login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        response = requests.post('http://127.0.0.1:8000/api/token/', data={'username': username, 'password': password})

        if response.status_code == 200:
            tokens = response.json()
            request.session['access'] = tokens.get('access')
            request.session['refresh'] = tokens.get('refresh')
            messages.success(request, "Login successful!")
            # redirect to site index/home page
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')