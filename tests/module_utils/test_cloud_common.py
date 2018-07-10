#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2018, Ricardo Carrillo Cruz <ricarril@redhat.com>
# (c) 2018, Yanis Guenane <yguenane@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from module_utils.cloud_common import _parse_configuration, sanitize_provider, sanitize_action, sanitize_args


def test_sanitize_provider_mangled():
    assert sanitize_provider('vultr') == 'vr'
    assert sanitize_provider('openstack') == 'os'


def test_sanitize_provider_unmangled():
    assert sanitize_provider('aws') == 'aws'
    assert sanitize_provider('digital_ocean') == 'digital_ocean'


def test_sanitize_action_mangled():
    assert sanitize_action('vultr', 'sshkey') == 'ssh_key'


def test_sanitize_action_unmangled():
    assert sanitize_action('digital_ocean', 'sshkey') == 'sshkey'


def test_sanitize_args_mangled():
    assert sanitize_args('digital_ocean', 'cloud_sshkey', 'sshkey') == 'ssh_pub_key'


def test_sanitize_args_unmangled():
    assert sanitize_args('digital_ocean', 'cloud_sshkey', 'name') == 'name'


def test_parse_configuration_valid():

    data = {'provider': 'vultr', 'api_key': 'TOKEN'}
    config = """
[defaults]
provider = %s

[vultr]
api_key=%s
    """ % (data['provider'], data['api_key'])

    _config = _parse_configuration(config)

    assert _config['provider'] == data['provider']
    assert _config['configuration']['api_key'] == data['api_key']
