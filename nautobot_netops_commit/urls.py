"""Urls for netops_commit."""

from django.urls import path

from nautobot_netops_commit import views

urlpatterns = [
    path("changes/", views.NetopsCommitChangesView.as_view(), name="changes"),
    path("configuration/", views.NetopsCommitConfigurationView.as_view(), name="config"),
]
