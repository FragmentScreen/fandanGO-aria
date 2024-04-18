
## Intro

Welcome to the FandanGO ARIA plugin.

This package acts as a broker for ARIA's data deposition REST endpoints.

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

