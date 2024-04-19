


<div align="center">
  <img src="https://instruct-eric.org/upload/KIZ6uJYFfVnfSmcXqOrm6vuceCTUiYdT.png" alt="Alt text" width="200" margin='auto'>
  <h1>FandanGO : Aria Plugin</h1>
</div>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



[![Connect on LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue.svg)](https://www.linkedin.com/company/instruct-eric/mycompany/)
[![GitHub issues](https://img.shields.io/github/issues/FragmentScreen/fandango-aria-plugin)](https://github.com/FragmentScreen/fandango-aria-plugin/issues)
[![GitHub forks](https://img.shields.io/github/forks/FragmentScreen/fandango-aria-plugin)](https://github.com/FragmentScreen/fandango-aria-plugin/network/members)
[![GitHub contributors](https://img.shields.io/github/contributors/FragmentScreen/fandango-aria-plugin)](https://github.com/FragmentScreen/fandango-aria-plugin/graphs/contributors)
[![PyPI version](https://badge.fury.io/py/fandango-aria-plugin.svg)](https://badge.fury.io/py/fandango-aria-plugin)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/Documentation-Wiki-brightgreen)](https://github.com/FragmentScreen/fandango-aria-plugin/wiki)



## Intro

Welcome to the FandanGO ARIA plugin.

This package acts as a broker for ARIA's data deposition REST endpoints.

Please refer to our [Wiki](https://github.com/FragmentScreen/fandango-aria-plugin/wiki) for full documentation. 

## Installation

Install via [PYPI](https://pypi.org/project/fandango-aria-plugin)

`pip install fandango-aria-plugin`


### Note

This package uses [Keyring](https://pypi.org/project/keyring) to store token information securely.
Keyring is usable accross multiple os and supports the following backends:

- macOS Keychain
- Freedesktop Secret Service supports many DE including GNOME (requires [secretstorage](https://pypi.org/project/SecretStorage/))
- KDE4 & KDE5 KWallet (requires dbus)
- Windows Credential Locker

**Linux**

If problems arise when storing tokens on a Linux device, it may be required to download `dbus-python`.

Please use the [dbus package](https://pypi.org/project/dbus-python/) to solve the issue

## Setup

Connections are configured in the `config.yml` file located within the `fandango/config` package.

Here, you will be required to complete the following:

### All Connections

- Login URL
    - Note: You will need slgihtly different URLS for BETA/LOCAL token retrieval 
- Client Secret
- Client ID
- Session Key
- Facility ID

### Local Connections

- *Local* Data Deopsition Base
- *Local* Entity Base

### Beta Connections

- *Beta* Data Deopsition Base
- *Beta* Entity Base

### Caveats

The following config options are not neccessary and are mostly used for development : 

- Email : If a CLI user, this will remove the need to re-enter your login email
- Password : Similar to Email. Use with caution if on a communal computer.
- Username

### Post Setup

If you've successfully completed the above setup options, you're ready to start using the package.

If at any point you need to switch between Local and Beta databases, switch the `DEV` value between `LOCAL` and `BETA` 







