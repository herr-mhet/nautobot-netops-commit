"""Model definition for netops_commit."""

from django.db import models
from django.conf import settings

from nautobot.dcim.models import DeviceRole
from nautobot.apps.models import OrganizationalModel,extras_features


@extras_features(
    "webhooks",
)
class Commit(OrganizationalModel):
    """Commits are collections of Change Logs that have been approved for 
    publishing and deployment unto the automated network"""

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            null=True,
            on_delete=models.SET_NULL,
        )

    def __str__(self):
        return "Commit deployed on " + self.timestamp.strftime("%d.%m.%Y at  %H:%M:%S")

