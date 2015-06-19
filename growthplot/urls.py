"""growthplot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^growthplot/', include('growthplot.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login),
    url(r'^logout', views.logout_user),
    url(r'^register', views.register),
    url(r'^child', views.child),
    url(r'^profile', views.profile),
    url(r'^chart', views.chart),
    url(r'^data', views.child_profile),
    url(r'^enterlog', views.enter_log),
    url(r'^about', views.about)
    #url(r'^standard_curve_example$', views.standard_curve_example),
    #url(r'^admin/', include(admin.site.urls)),
]
