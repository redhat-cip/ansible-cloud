#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2018, Ricardo Carrillo Cruz <ricarril@redhat.com>
# (c) 2018, Yanis Guenane <yguenane@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import ConfigParser
import os
import StringIO


def sanitize_provider(provider):
    association = {
        'vultr': 'vr',
        'openstack': 'os'
    }

    return association.get(provider, provider)


def sanitize_action(provider, action):
    association = {
        'vultr': {
            'sshkey': 'ssh_key'
        }
    }

    provider_translation = association.get(provider, None)
    if not provider_translation:
        return action

    return provider_translation.get(action, action)


def sanitize_args(provider, action, args):
    association = {
        'cloud_sshkey': {
            'sshkey': {
                'digital_ocean': 'ssh_pub_key',
                'vultr': 'ssh_key'
            },
            'api_key': {
                'digital_ocean': 'oauth_token'
            }
        }
    }

    args_translation = association.get(action).get(args, None)
    if not args_translation:
        return args

    provider_translation = args_translation.get(provider, None)
    if not provider_translation:
        return args

    return provider_translation


def _load_configuration():
    configuration_file = os.environ.get(
        'ANSIBLE_CLOUD_CONFIG', os.path.expanduser('~/.ansible_cloud.cfg')
    )

    # TODO(Spredzy): Run the following in a try/catch to fail cleanly if the
    #                file does not exist
    return open(configuration_file).read()


# TODO(spredzy): Properly handle misconfiguration based on the provider type
def _parse_configuration(configuration):
    _configuration = StringIO.StringIO(configuration)
    config = ConfigParser.ConfigParser()
    config.readfp(_configuration)

    provider = config.get('defaults', 'provider', None)
    api_key = config.get(provider, 'api_key', None)

    return {
        'provider': provider,
        'configuration': {
            'api_key': api_key
        }
    }
