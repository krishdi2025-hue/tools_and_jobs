from django.urls import path
from . import views

from accounts.views import CustomTokenObtainPairView
# from .views import login_view,logout_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('token/refresh/', views.refresh_token_view, name='token_refresh_view'),
    path('dashboard/', views.dashboard_view, name='dashboard'), 
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
