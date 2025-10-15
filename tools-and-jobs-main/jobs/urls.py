from django.urls import path
from . import views


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', views.jobs, name='jobs'),
    path('engineering/',views.engineering,name='engineering'),
    path('business/', views.business, name='business'),
    path('sales/', views.sales, name='sales'),
    path('communication/', views.communication, name='communication'),
    path('search1/', views.search1, name='search1'),

]
