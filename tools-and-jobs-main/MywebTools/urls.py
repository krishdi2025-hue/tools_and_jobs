"""MywebTools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include


from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .sitemaps import StaticViewSitemap
from .sitemaps import TestSitemap
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


sitemaps = {
    'static':StaticViewSitemap,

    'testpost':TestSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webtools1.urls')),
    path('signup/', include('signup.urls')),
   
    path('engifree/', include('engifree.urls')),
    path('jobs/', include('jobs.urls')),
    path('mcq/', include('techmcq.urls')),
    path('url', include('URLshortner.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('pushbots-worker.js', TemplateView.as_view(template_name= 'pushbots-worker.js', content_type = 'text/javascript')),
    path('robots.txt',TemplateView.as_view(template_name = 'robots.txt', content_type = 'text/plain'),),
    path('ads.txt', TemplateView.as_view(template_name='ads.txt', content_type='text/plain'), ),
    path('ckeditor/',include('ckeditor_uploader.urls')),

    path('register/', include('register.urls')),
    # login app
    path('login/', include('login.urls')),

              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

