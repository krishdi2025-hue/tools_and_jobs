from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs, name='jobs'),
    path('add/', views.add_job, name='jobs_add'),
]
