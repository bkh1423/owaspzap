from django.db import models
from scans.models import ScanJob


class Vulnerability(models.Model):
    """
    A single alert/vulnerability returned by OWASP ZAP for a given scan job.
    """
    SEVERITY_CHOICES = [
        ("informational", "Informational"),
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    scan_job = models.ForeignKey(ScanJob, on_delete=models.CASCADE, related_name="vulnerabilities")

    name = models.CharField(max_length=255)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default="informational")

    description = models.TextField(blank=True)
    solution = models.TextField(blank=True)

    evidence = models.TextField(blank=True)
    reference = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.severity})"


class Report(models.Model):
    """
    Represents an exported report for a scan.
    """
    scan_job = models.ForeignKey(ScanJob, on_delete=models.CASCADE, related_name="reports")

    title = models.CharField(max_length=255, default="Security Scan Report")
    format = models.CharField(max_length=10, default="pdf")  # pdf/csv later
    file_path = models.CharField(max_length=500, blank=True)  # store generated file path

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Report #{self.id} for ScanJob #{self.scan_job.id}"
