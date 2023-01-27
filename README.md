# Nautobot NetOps Commit Plugin

A plugin for [Nautobot](https://github.com/nautobot/nautobot) that is meant to 
provide a deploy mechanism for network operations: Whenever a change on a 
device in Nautobot has been made that is then meant to be transferred onto 
the actual device, the user can click on a button on the device's page that 
starts the deployment operations.

## Installation

The plugin is available as a Python package in PyPI and can be installed with 
`pip`:

```shell
pip install nautobot_netops_commit
```

> The plugin is compatible with Nautobot 1.5.9 and higher

To ensure Nautobot Firewall Models Plugin is automatically re-installed during 
future upgrades, create a file named `local_requirements.txt` (if not already 
existing) in the Nautobot root directory (alongside `requirements.txt`) and list 
the `nautobot_netops_commit` package:

```no-highlight
# echo nautobot_netops_commit >> local_requirements.txt
```

Once installed, the plugin needs to be enabled in your `nautobot_config.py`

```python
# In your nautobot_config.py
PLUGINS = ["nautobot_netops_commit"]
```

It currently also requires certain plugin configurations to be inserted into 
your `nautobot_config.py`

```python
PLUGINS_CONFIG = {
    "nautobot_netops_commit": {
        "watched_device_role_uid": "00000000-0000-0000-0000-000000000000"
    }
}
```

## How it works

The plugin adds a "Commit & Deploy" button at the top-right button collection 
in Nautobot. When pressed it creates a new Commit object that stores some 
metadata. This is then meant to be used in conjunction with Nautobot's webhook 
capabilities, so that whenever a new Commit object has been created, a webhook
is called.

To prevent this button to be seen on any kind of device, this plugin uses the 
`watched_device_role_uid` setting (see above) to only display on devices that 
belong to that device role.

Currently the Commit objects only store the current timestamp and the user 
that pressed the button. It is planned that this plugin taps into Nautobot's 
changelog feature so that each Commit can list all of the changes made to the 
device(s) being watched. 

How to create a webhook receiver is out of the scope of this document and 
depends on your specific environment.

## Disclaimer

This plugin is meant to be used with Nautobot but is otherwise not affiliated 
with the Nautobot product or the Network to Code LLC. Use at your own risk.

