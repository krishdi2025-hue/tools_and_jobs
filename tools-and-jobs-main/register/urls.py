from django.urls import path
from .views import register_company_page,company_login_page,register_company_page,register_company

urlpatterns = [

    path('', register_company_page, name='company_register'),
    path('api/register/', register_company, name='register_api'), # API endpoint
    path('login', company_login_page, name="compnay_login")
]
