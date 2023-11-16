ipfabric_nornir
==============

## About

Founded in 2015, [IP Fabric](https://ipfabric.io/) develops network infrastructure visibility and analytics solution to
help enterprise network and security teams with network assurance and automation across multi-domain heterogeneous
environments. From in-depth discovery, through graph visualization, to packet walks and complete network history, IP
Fabric enables to confidently replace manual tasks necessary to handle growing network complexity driven by relentless
digital transformation.

# Special Thanks

This project is an IP Fabric officially supported fork of 
[nornir_ipfabric](https://github.com/routetonull/nornir_ipfabric) by [routetonull](https://github.com/routetonull/).


# Install

The recommended way to install `ipfabric_nornir` is via pip

```sh
pip install ipfabric_nornir
```

# Requirements

An instance of [IP Fabric](https://ipfabric.io/) is required to collect information. [Request trial license.](https://ipfabric.io/booking-trial/)


# Example usage

## Setup

### Using environment variables

Set environment vars to provide url and credentials to connect to the IP Fabric server

```sh
export IPF_URL=https://ipfabric.local
export IPF_TOKEN=myToken

# Or Username and Password
export IPF_USER=admin
export IPF_PASSWORD=mySecretPassword
```

### Using `.env` file

The easiest way to use this package is with a `.env` file.  You can copy the sample and edit it with your environment variables. 

```commandline
cp sample.env .env
```

This contains the following variables which can also be set as environment variables instead of a .env file.
```
IPF_URL="https://demo3.ipfabric.io"
IPF_TOKEN=TOKEN
IPF_VERIFY=true
```

Or if using Username/Password:
```
IPF_URL="https://demo3.ipfabric.io"
IPF_USERNAME=USER
IPF_PASSWORD=PASS
```

## Running

```python
from nornir import InitNornir
nr = InitNornir(inventory={"plugin": "IPFabricInventory"})
```


## Using the InitNornir function

Init

```python
from nornir import InitNornir
nr = InitNornir(
    inventory=
        {
            "plugin": "IPFabricInventory", 
            "options": {
                "base_url":"https://ipfabric.local",
                "token":"myToken",
                # "username":"admin",
                # "password":"mySecretPassword",
                },
        },
    )
```

## Using the Nornir configuration file

File *config.yaml*

```yaml
---
inventory:
  plugin: IPFInventory
  options:
    base_url: "https://ipfabric.local"
    token: "myToken"
    # username: "admin"
    # password: "mySecretPassword"
```

Usage:

```python
from nornir import InitNornir
nr = InitNornir(config_file="config.yaml",inventory={"plugin": "IPFabricInventory"})
```
