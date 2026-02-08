from django.contrib import admin
from .models import Vulnerability, Report


@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ("name", "severity", "scan_job", "created_at")
    list_filter = ("severity", "created_at")
    search_fields = ("name", "scan_job__target__url")
    ordering = ("-created_at",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "format", "scan_job", "created_at")
    list_filter = ("format", "created_at")
    search_fields = ("title", "scan_job__target__url")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
