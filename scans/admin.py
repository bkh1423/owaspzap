from django.contrib import admin
from .models import Target, ScanJob, ScanSchedule


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ("url", "owner", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("url", "owner__username", "owner__email")
    ordering = ("-created_at",)


@admin.register(ScanJob)
class ScanJobAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "target",
        "status",
        "requested_by",
        "created_at",
        "started_at",
        "finished_at",
    )
    list_filter = ("status", "created_at", "started_at", "finished_at")
    search_fields = ("target__url", "requested_by__username", "requested_by__email")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


@admin.register(ScanSchedule)
class ScanScheduleAdmin(admin.ModelAdmin):
    list_display = ("target", "frequency", "enabled", "next_run_at", "created_at")
    list_filter = ("enabled", "frequency", "created_at")
    search_fields = ("target__url",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
