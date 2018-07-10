#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2018, Ricardo Carrillo Cruz <ricarril@redhat.com>
# (c) 2018, Yanis Guenane <yguenane@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import copy

from ansible.plugins.action import ActionBase
from ansible.module_utils.cloud_common import _load_configuration, _parse_configuration, sanitize_provider, sanitize_action, sanitize_args


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        del tmp  # tmp no longer has any effect
        if task_vars is None:
            task_vars = dict()

        play_context = copy.deepcopy(self._play_context)
        play_context.provider = self._get_provider()

        module = self._get_implementation_module(
            play_context.provider, self._task.action
        )

        self._task.args.update({'api_key': self._get_api_key()})
        sanitized_args = dict()
        for key, value in self._task.args.items():
            sanitized_args[sanitize_args(play_context.provider, self._task.action, key)] = value

        result = super(ActionModule, self).run(task_vars=task_vars)
        result.update(self._execute_module(
            module_name=module, module_args=sanitized_args, task_vars=task_vars
        ))

        return result

    def _get_provider(self):
        return _parse_configuration(_load_configuration())['provider']

    def _get_api_key(self):
        return _parse_configuration(_load_configuration())['configuration']['api_key']

    def _get_implementation_module(self, provider, cloud_agnostic_module):

        _provider = sanitize_provider(provider)
        _action = sanitize_action(provider, '_'.join(cloud_agnostic_module.split('_')[1:]))

        implementation_module = '%s_%s' % (_provider, _action)
        if implementation_module not in self._shared_loader_obj.module_loader:
            implementation_module = None

        return implementation_module
