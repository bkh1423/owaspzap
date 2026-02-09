from django.urls import path
from .views import scan_test

urlpatterns = [
    path('test/', scan_test, name='scan-test'),
]
