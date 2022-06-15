from django.db import models
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager, ActiveUsersManager

# Create your models here.
class CustomUser(AbstractUser):
    """Customize django default user authentication model"""

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Managers
    objects = CustomUserManager()
    active_users = ActiveUsersManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
