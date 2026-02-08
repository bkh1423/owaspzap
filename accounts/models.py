from django.db import models
from django.conf import settings


class Role(models.Model):
    """
    Simple role model (do NOT name the app as 'User' or 'Admin').
    This keeps roles flexible without replacing Django's default User model.
    """
    name = models.CharField(max_length=50, unique=True)  # e.g., "ADMIN", "ANALYST"
    description = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name


class UserRole(models.Model):
    """
    Link Django User to a Role.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "role")

    def __str__(self) -> str:
        return f"{self.user} -> {self.role}"
