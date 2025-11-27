from django.urls import path
from . import views
from accounts.views import CustomTokenObtainPairView
# from .views import login_view,logout_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('token/refresh/', views.refresh_token_view, name='token_refresh_view'),
    path('Profile/', views.Profile_view, name='Profile'), 
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
       
   

]
