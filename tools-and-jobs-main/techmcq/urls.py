from . import views
from django.urls import path
from .models import Category
from django.views.generic import RedirectView
urlpatterns = [


    #urls for test
    
    path('', views.TestList.as_view(), name='mcq'),
    path('searchmcq/', views.SearchResultsView.as_view(), name='searchmcq'),
    path('<slug:slug1>/', views.TestDetail.as_view(), name='test_detail'),
    path('category/<category>',views.CatListView.as_view(), name = "category"),


]