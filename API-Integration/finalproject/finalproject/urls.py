"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
	url(r'home_page', TemplateView.as_view(template_name='home_page.html'), name='home_page'),
    url(r'bootstrap', TemplateView.as_view(template_name='bootstrap/example.html'), name='example'),	
	url('^', include('django.contrib.auth.urls')),
	url(r'^database/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'userapp/', include('userapp.urls')),
    url(r'userapp/', include('django.contrib.auth.urls'))
]

