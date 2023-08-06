# pytest-rocketchat
Pytest to [RocketChat](https://github.com/RocketChat) reporting plugin.

[![pypi](https://img.shields.io/pypi/v/pytest-rocketchat.svg)](https://pypi.org/project/pytest-rocketchat/)

___Inspired by [pytest-slack](https://pypi.org/project/pytest-slack/) & [pytest-messenger](https://pypi.org/project/pytest-messenger/).___

## Usage
```
$ pytest --rocketchat_domain=https://your.chat --rocketchat_username=username --rocketchat_password=password --rocketchat_channel=channel
```
Options:
- --rocketchat_domain* (Required)
- --rocketchat_username* (Required)
- --rocketchat_password* (Required)
- --rocketchat_channel* (Required)  
- --rocketchat_report_link
- --rocketchat_message_prefix
- --rocketchat_timeout
- --rocketchat_success_emoji
- --rocketchat_failed_emoji
- --ssl_verify

## Requirements
- Python >= 3.6
- Requests
- Rocketchat_API

## Installation
You can install "pytest-rocketchat" via [pip](https://pypi.python.org/pypi/pip/):
```
$ pip install pytest-rocketchat
```
If you encounter any problems, please file an [issue](https://github.com/aleksandr-kotlyar/pytest-rocketchat/issues) along with a detailed description.
