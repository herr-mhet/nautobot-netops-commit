from rest_framework.viewsets import ModelViewSet

from nautobot_netops_commit.models import Commit
from .serializers import CommitSerializer


class CommitViewSet(ModelViewSet):
    """API viewset for interacting with Commit objects."""

    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
