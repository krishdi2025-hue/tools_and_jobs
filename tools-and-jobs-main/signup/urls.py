from django.urls import path
from . import views


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', views.suscribe, name='suscribe'),
    path('contactus/',views.contactus,name='contactus'),

]

