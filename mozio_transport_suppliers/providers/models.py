from django.db import models
import uuid
from django.utils.translation import gettext as _
from typing import Optional
from phone_field import PhoneField
from .currencies import CURRENCIES
from .languages import LANGUAGES


class Provider(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    name = models.CharField(_("Provider Name"), max_length=255)
    email = models.EmailField(_("Provider Email"), unique=True, max_length=255)
    currency = models.CharField(
        _("Provider Currency"), choices=CURRENCIES, max_length=10, default="$"
    )
    language = models.CharField(
        _("Provider Language"), max_length=40, choices=LANGUAGES, default="en"
    )
    phone_number = PhoneField(
        _("Provider Phone Number"), help_text="Contact phone number"
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "providers"
        ordering = ("name", "email")
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")

    def __str__(self):
        return f"{self.name} - {self.email}"

    def get_provider_email(self) -> Optional[str]:
        return self.user.email if self.user else self.email
