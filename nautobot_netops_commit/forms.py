from django import forms

from nautobot.extras.forms import NautobotModelForm
from nautobot.utilities.forms import (
    BootstrapMixin,
    BulkEditForm,
    CSVModelForm,
)
from nautobot.dcim.models import DeviceRole

class NetopsCommitConfigurationForm(BootstrapMixin, forms.Form):
    """plugin-specific configuration"""

    device_role = forms.ModelChoiceField(
        DeviceRole.objects.all(),
        help_text="Device role to collect commits for",
    )

class NetopsCommitDeployChangeForm(BootstrapMixin, forms.Form):
    device = forms.UUIDField(widget=forms.HiddenInput())

