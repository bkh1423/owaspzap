"""
URL configuration for owaspzap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Redirect root URL "/" to admin (temporary, no custom views)
    path('', RedirectView.as_view(url='/admin/', permanent=False)),

    path('admin/', admin.site.urls),

    # Project apps routes
    path('api/accounts/', include('accounts.urls')),
    path('api/scans/', include('scans.urls')),
    path('api/reporting/', include('reporting.urls')),
]
