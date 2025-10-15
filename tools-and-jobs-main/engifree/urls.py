from django.urls import path
from . import views



urlpatterns = [

    # Uncomment the next line to enable the admin:
    path('', views.engifree, name='engifree'),
    path('learnfree/', views.learnfree, name='learnfree'),
    path('search/', views.search, name='search'),
]
