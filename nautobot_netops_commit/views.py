"""Views for netops_commit."""

from django.shortcuts import render
from nautobot.core.views import generic
from django.conf import settings

from nautobot.extras.models import ObjectChange
from nautobot_netops_commit import models,forms
from nautobot_netops_commit.api import serializers

class NetopsCommitConfigurationView(generic.View):
    """Provides a form for plugin configuration settings."""

    def get(self, request):
        form = forms.NetopsCommitConfigurationForm()
        return render(request, "nautobot_netops_commit/config.html", {"form": form})

    def post(self, request):
        form = forms.NetopsCommitConfigurationForm(request.POST)
        if form.is_valid():
            pprint(form.cleaned_data["device_role"])
        return render(request, "nautobot_netops_commit/config.html", {"form": form})

class NetopsCommitChangesView(generic.View):
    """Displays (recent) changes on matched objects."""

    recent_changes = ObjectChange.objects.all()

    def get(self, request):
        all_commits = models.Commit.objects.all()
        return render(request, 'nautobot_netops_commit/changes.html', {
            "changes": all_commits,
        })

    def post(self, request):
        form = forms.NetopsCommitDeployChangeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data) # TODO
            new_commit = models.Commit()
            new_commit.user = request.user
            new_commit.save()

        all_commits = models.Commit.objects.all()
        return render(request, 'nautobot_netops_commit/changes.html', {
            "changes": all_commits,
        })

