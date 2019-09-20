# Some examples are given below.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dhcpd_conf_file(host):
    file = host.file('/etc/dhcp/dhcpd.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


# def test_dhcpd_failover_conf_file(host):
#     file = host.file('/etc/dhcp/dhcpd-failover.conf')
#
#     assert file.exists
#     assert file.user == 'root'
#     assert file.group == 'root'


def test_dhcpd_keys_conf_file(host):
    file = host.file('/etc/dhcp/dhcpd-keys.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_dhcpd_networks_conf_file(host):
    file = host.file('/etc/dhcp/dhcpd-networks.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_dhcpd_groups_conf_file(host):
    file = host.file('/etc/dhcp/dhcpd-groups.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_dhcpd_omapi_conf_file(host):
    file = host.file('/etc/dhcp/dhcpd-omapi.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_dhcp_service(host):
    srv = host.service('dhcpd')

    assert srv.is_running
    assert srv.is_enabled
