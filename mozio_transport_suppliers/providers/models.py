from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext as _

import uuid
from phone_field import PhoneField
from typing import Optional

from .currencies import CURRENCIES
from .languages import LANGUAGES


class Provider(models.Model):

    """
    Provider user profile.

    Signal: When user is registered in the system the provider profile is created with the following fields.
    Allow to create a new provider profile for a new user.

    If name is changed, the name is updated in the provider profile.

    """

    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        unique=True,
        on_delete=models.CASCADE,
        related_name="provider",
    )

    name = models.CharField(_("Provider Name"), max_length=255)
    email = models.EmailField(
        _("Provider Email"), editable=False, unique=True, max_length=255
    )
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


class ServiceArea(models.Model):
    """
    Service Area model.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="service_areas"
    )
    name = models.CharField(_("Service Area Name"), max_length=100)
    price = models.DecimalField(
        _("Service Area Price"), max_digits=50, decimal_places=2
    )
    geo_json = models.JSONField(_("Polygon coordinates"))

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "service_areas"
        ordering = ("name", "provider")
        verbose_name = _("Service Area")
        verbose_name_plural = _("Service Areas")

    def __str__(self):
        return f"{self.provider.name} - {self.name}"
