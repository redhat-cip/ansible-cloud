#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2018, Ricardo Carrillo Cruz <ricarril@redhat.com>
# (c) 2018, Yanis Guenane <yguenane@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = r'''
---
module: cloud_sshkey
short_description: Manage SSH key pair on a cloud provider.
description:
  - Manage SSH key pair on a cloud provider.
version_added: "2.7"
author:
  - Ricardo Carrillo Cruz (@rcarrillocruz)
  - Yanis Guenane (@Spredzy)
options:
  api_key:
    description:
      - Specified the token to use with the API call
      - This value can be configured in ~/.ansible_cloud.cfg
  name:
    description:
      - Specifies the name of the key
    required: true
  sshkey:
    description:
      - The public SSH key
    required: true
  state:
    description:
      - Specifies whether or not the SSH key should be present
    default: present
    choices: ['present', 'absent']
'''

EXAMPLES = r'''
- name: Create a SSH key
  cloud_sshkey:
    name: me@home
    content: YOURSSHKEY

- name: Destroy a SSH key
  cloud_sshkey:
    name: me@home
    sate: absent
'''

RETURN = r'''
---
cloud_sshkey:
  description: Response from the cloud provider API
  returned: success
  type: complex
  contains:
    id:
      description: The ID of the SSH key
      returned: success
      type: string
      sample: 42024
    name:
      description: The name of the SSH key
      returned: success
      type: string
      sample: me@home
    sshkey:
      description: The SSH key
      returned: success
      type: string
      sample: ssh-rsa AA... me@home
'''
