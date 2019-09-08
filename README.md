<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_dhcp.svg)](https://github.com/while-true-do/ansible-role-srv_dhcp/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_dhcp.svg)](https://github.com/while-true-do/ansible-role-srv_dhcp/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_dhcp.svg)](https://github.com/while-true-do/ansible-role-srv_dhcp/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_dhcp.svg)](https://github.com/while-true-do/ansible-role-srv_dhcp/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_dhcp.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_dhcp)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_dhcp%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_dhcp)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_dhcp%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_dhcp)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_dhcp%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_dhcp)

# Ansible Role: srv_dhcp

An Ansible Role to install and configure dhcp servers.

## Motivation

DHCP is used in many networks and for PXE Deployments. Setting up and
configuring DHCP is a very common use case for many operators.

## Description

This Role installs and configures a DHCP Server.

- manage packages
- manage services
- manage firewall
- configure global configurations
- configure networks
- configure dhcp pools
- configure omapi
- configure dhcp failover

## Requirements

Used Modules:

-   [Ansible package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)
-   [Ansible firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
-   [Ansible template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible file Module](https://docs.ansible.com/ansible/latest/modules/file_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_dhcp)
```
ansible-galaxy install while_true_do.srv_dhcp
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_dhcp)
```
git clone https://github.com/while-true-do/ansible-role-srv_dhcp.git while_true_do.srv_dhcp
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_dhcp

## Package Management
wtd_srv_dhcp_package: "dhcp"
# State can be present|latest|absent
wtd_srv_dhcp_package_state: "present"

## Configuration Management
# see /usr/share/doc/dhcp-server/dhcpd.conf.example
# see dhcpd.conf(5) man page

# Configure global parameters (/etc/dhcpd.conf)
wtd_srv_dhcp_conf_global: []
# local_address: ""
# authoritative: false
# domain_name: ""
# domain_name_servers: ""
# ntp_servers: ""
# default_lease_time: 600
# max_lease_time: 7200
# allow_booting: false
# allow_bootp: false
# next_server: ""
# filename: ""
# log_facility: ""
# options: []

# Configure networks (/etc/dhcp/dhcpd.conf)
wtd_srv_dhcp_conf_networks: []
# - name: ""
#   subnet: ""
#   netmask: ""
#   routers: ""
#   broadcast_address: ""
#   domain_name: ""
#   domain_name_servers: ""
#   max_lease_time: ""
#   options: []
#   range: ""
#   pools:
#   - name: ""
#     failover_peer: ""
#     range: ""
#     domain_name: ""
#     domain_name_servers: ""
#     max_lease_time: ""
#     unknown_clients: ""
#     options: []

# Configure Groups
wtd_srv_dhcp_conf_groups: []
#   - name: ""
#     use_host_decl_names: "on"
#     hosts:
#     - name: ""
#       hardware_ethernet: ""
#       fixed_address: ""

# Configure failover (/etc/dhcp/dhcpd-failover.conf)
wtd_srv_dhcp_conf_failover:
  enabled: false
# name: "dhcp-cluster"
# primary: true
# address: ""
# port: 647
# peer_address: ""
# peer_port: 647
# max_response_delay: 60
# max_unacked_updates: "10"
# load_balance_max_seconds: 3
# mclt: 1800
# split: 255

# Configure the omapi (/etc/dhcp/dhcpd-omapi.conf)
# You have to generate the secret via:
# $ dnssec-keygen -a HMAC-MD5 -b 128 -n USER DHCP_UPDATER
wtd_srv_dhcp_conf_omapi:
  enabled: false
# port: 7911
# key: "omapi_key"
# algorithm: "hmac-md5"
# secret: ""

# Configure additional file includes
wtd_srv_dhcp_conf_includes: []
# - path-to-file-1
# - path-to-file-2

## Service Management
wtd_srv_dhcp_service: "dhcpd"
# State can be started|stopped
wtd_srv_dhcp_service_state: "started"
wtd_srv_dhcp_service_enabled: true

## Firewalld Management
wtd_srv_dhcp_fw_mgmt: true
wtd_srv_dhcp_fw_service: "dhcp"
# State can be enabled|disabled
wtd_srv_dhcp_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_dhcp_fw_zone: "public"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

A dhcp server for 192.168.0.0/24 can look like.

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_dhcp
      wtd_srv_dhcp_conf_networks:
        - name: "my network"
          subnet: "192.168.0.0"
          netmask: "255.255.255.0"
          domain_name_servers: "192.168.0.1"
          routers: "192.168.0.1"
          range: "192.168.0.10 192.168.0.20"
```

#### Advanced

Define multiple pools and networks or change some global values.

```
- hosts: all
  roles:
    - role: while_true_do.srv_dhcp
      wtd_srv_dhcp_conf_global:
        authoritative: true
        domain_name: "example.net"
      wtd_srv_dhcp_conf_networks:
        - name: "my network 1"
          subnet: "192.168.0.0"
          netmask: "255.255.255.0"
          domain_name_servers: "192.168.0.1"
          routers: "192.168.0.1"
          pools:
            - name: "my network 1 pool"
              range: "192.168.0.10 192.168.0.20"
            - name: "my other network 1 pool"
              range: "192.168.0.100 192.168.0.250"
        - name: "my network 2"
          subnet: "192.168.10.0"
          netmask: "255.255.255.0"
          domain_name_servers: "192.168.10.1"
          routers: "192.168.10.1"
          range: "192.168.10.10 192.168.10.20"
```

Configure a dhcp cluster, enable the omapi and configure
a pool with the range 192.168.0.100 - 192.168.0.200.

Be aware, that you have to generate the omapi secret on your own and copy
the key.

```
# Generate omapi key
dnssec-keygen -a HMAC-MD5 -b 128 -C -n USER DHCP_UPDATER
cat *.key
# copy / paste the key
```

```
---
# dhcp_primary has ip address 192.168.0.11
- hosts: dhcp_primary
  roles:
    - role: while_true_do.srv_dhcp
      wtd_srv_dhcp_conf_networks:
        - name: "my network"
          subnet: "192.168.0.0"
          netmask: "255.255.255.0"
          domain_name_servers: "192.168.0.1"
          routers: "192.168.0.1"
          range: "192.168.0.100 192.168.0.200"
      wtd_srv_dhcp_conf_omapi:
        enabled: true
        secret: "my_secret!!!"
      wtd_srv_dhcp_conf_failover:
        enabled: true
        primary: true
        address: "192.168.0.11"
        peer_address: "192.168.0.12"

# dhcp_secundary has ip address 192.168.0.12
- hosts: dhcp_secundary
  roles:
    - role: while_true_do.srv_dhcp
      wtd_srv_dhcp_conf_networks:
        - name: "my network"
          subnet: "192.168.0.0"
          netmask: "255.255.255.0"
          domain_name_servers: "192.168.0.1"
          routers: "192.168.0.1"
          range: "192.168.0.100 192.168.0.200"
      wtd_srv_dhcp_conf_omapi:
        enabled: true
        secret: "my_secret!!!"
      wtd_srv_dhcp_conf_failover:
        enabled: true
        primary: false
        address: "192.168.0.12"
        peer_address: "192.168.0.11"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_dhcp/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_dhcp/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
