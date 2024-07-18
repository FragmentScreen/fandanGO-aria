


<div align="center">
  <img src="https://instruct-eric.org/upload/KIZ6uJYFfVnfSmcXqOrm6vuceCTUiYdT.png" alt="Alt text" width="200" margin='auto'>
  <h1>fandanGO-aria</h1>
</div>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



[![Connect on LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue.svg)](https://www.linkedin.com/company/instruct-eric/mycompany/)
[![GitHub issues](https://img.shields.io/github/issues/FragmentScreen/fandanGO-aria)](https://github.com/FragmentScreen/fandanGO-aria/issues)
[![GitHub forks](https://img.shields.io/github/forks/FragmentScreen/fandanGO-aria)](https://github.com/FragmentScreen/fandanGO-aria/network/members)
[![GitHub contributors](https://img.shields.io/github/contributors/FragmentScreen/fandanGO-aria)](https://github.com/FragmentScreen/fandanGO-aria/graphs/contributors)
[![PyPI version](https://badge.fury.io/py/fandanGO-aria.svg)](https://badge.fury.io/py/fandanGO-aria)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/Documentation-Wiki-brightgreen)](https://github.com/FragmentScreen/fandanGO-aria/wiki)



## Intro

Welcome to the fandanGO-aria package.

This package acts as a broker for ARIA's metadata deposition REST endpoints.

Please refer to our [Wiki](https://github.com/FragmentScreen/fandanGO-aria/wiki) for full documentation. 

## Installation

Install via [PYPI](https://pypi.org/project/fandanGO-aria)

`pip install fandanGO-aria`


## Setup

Connections are configured in the `.env` file located in the root of your project.

Here, you will be required to complete the following:

### All Connections

- Login URL
    - Note: You will need slgihtly different URLS for BETA/LOCAL token retrieval 
- Client Secret
- Client ID
- Grant Type
- Scope
- Session Key
- Facility ID


### Caveats

The following `env` options are not neccessary and are mostly used for development : 

- Email : If a CLI user, this will remove the need to re-enter your login email
- Password : Similar to Email. Use with caution if on a communal computer.
- Username

### Post Setup

If you've successfully completed the above setup options, you're ready to start using the package.


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



