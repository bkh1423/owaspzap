from django.db import models
from django.conf import settings


class Target(models.Model):
    """
    Target website to scan.
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="targets")
    url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.url


class ScanJob(models.Model):
    """
    Represents one scanning run triggered by user or schedule.
    """
    STATUS_CHOICES = [
        ("queued", "Queued"),
        ("running", "Running"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name="scan_jobs")
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="scan_requests")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="queued")

    # Optional: store ZAP scan IDs
    zap_spider_id = models.CharField(max_length=64, blank=True)
    zap_ascan_id = models.CharField(max_length=64, blank=True)

    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    error_message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.target.url} [{self.status}]"


class ScanSchedule(models.Model):
    """
    Simple schedule for recurring scans (basic).
    Later you can integrate Celery Beat or APScheduler.
    """
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name="schedules")
    enabled = models.BooleanField(default=True)

    # basic scheduling (simple and clear)
    frequency = models.CharField(max_length=20, default="weekly")  # e.g. daily/weekly/monthly
    next_run_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.target.url} -> {self.frequency}"
