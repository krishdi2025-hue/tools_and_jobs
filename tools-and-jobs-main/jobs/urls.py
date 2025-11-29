from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.jobs, name="jobs_list"), 
    path('add/', views.add_job, name='jobs_add'),
    path("job/<int:pk>/edit/", views.edit_job, name="job_edit"),
    path("job/<int:pk>/delete/", views.delete_job, name="job_delete"),
    path("job/<int:pk>/", views.about_job, name="about_job"),
    
]
