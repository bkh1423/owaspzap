"""
URL configuration for owaspzap project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # مؤقت: حولي الصفحة الرئيسية للواجهة بدل الأدمن (أو خليها زي ما تبين)
    # لو تبينها للواجهة:
    path('', RedirectView.as_view(url='/scans/test/', permanent=False)),

    path('admin/', admin.site.urls),

    # صفحات الواجهات (Templates)
    path('scans/', include('scans.web_urls')),   # <-- جديد

    # API routes
    path('api/accounts/', include('accounts.urls')),
    path('api/scans/', include('scans.urls')),
    path('api/reporting/', include('reporting.urls')),
]
