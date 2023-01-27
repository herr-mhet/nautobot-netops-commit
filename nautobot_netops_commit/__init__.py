"""nautobot_netops_commit Plugin Initilization."""

from importlib import metadata
from nautobot.extras.plugins import PluginConfig

__version__ = metadata.version(__name__)

class NautobotNetopsCommitConfig(PluginConfig):
    """Plugin configuration for the netops_commit plugin."""

    name = "nautobot_netops_commit"  # Raw plugin name; same as the plugin's source directory.
    verbose_name = "NetOps Commit"  # Human-friendly name for the plugin.
    author = "Alexander Herr"
    author_email = "herr@eth.mpg.de"
    version = __version__
    description = "Provides commit capabilities for SSoT automation"
    base_url = "netops_commit"  # (Optional) Base path to use for plugin URLs. Defaulting to app_name.
    required_settings = (
        []
    )  # A list of any configuration parameters that must be defined by the user.
    min_version = (
        "1.0.0"  # Minimum version of Nautobot with which the plugin is compatible.
    )
    max_version = (
        "1.999"  # Maximum version of Nautobot with which the plugin is compatible.
    )
    default_settings = (
        {}
    )  # A dictionary of configuration parameters and their default values.
    required_settings = [
        "watched_device_role_uid",
    ]  # A list of any configuration parameters that must be defined by the user
    caching_config = {}  # Plugin-specific cache configuration.
    config_view_name = "plugins:nautobot_netops_commit:config"


config = NautobotNetopsCommitConfig
