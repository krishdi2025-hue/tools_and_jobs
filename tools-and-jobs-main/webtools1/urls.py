from django.urls import path
from . import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', views.index, name='index'),
    path('searchtoolsjobs/', views.searchtoolsjobs, name='searchtoolsjobs'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('about_us',views.about_us,name='about_us'),
    path('apks/<str:toolsandjobs>/', views.download_apk, name= 'download_apk'),
    path('downloadapk/', views.downloadapp, name = 'downloadapp'),
]

