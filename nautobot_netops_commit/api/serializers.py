from nautobot.apps.api import ValidatedModelSerializer

from nautobot_netops_commit.models import Commit


class CommitSerializer(ValidatedModelSerializer):
    """API serializer for the Commit class"""

    class Meta:
        model = Commit
        fields = ("user", "timestamp")
