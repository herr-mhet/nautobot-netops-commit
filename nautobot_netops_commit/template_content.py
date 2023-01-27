import uuid
from django.conf import settings
from nautobot.apps.ui import TemplateExtension
from nautobot_netops_commit import forms

class DeployButton(TemplateExtension):
    model = 'dcim.device'

    def buttons(self):
        dr_uid = uuid.UUID(settings.PLUGINS_CONFIG["nautobot_netops_commit"]["watched_device_role_uid"])
        if self.context["object"].device_role.id == dr_uid:
            form = forms.NetopsCommitDeployChangeForm()
            form.fields["device"].initial = self.context["object"].id
            return self.render(
                'nautobot_netops_commit/deploybutton.html',
                extra_context = {
                    'form': form,
            })
        return ""

template_extensions = [DeployButton]
