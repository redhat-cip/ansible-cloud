#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2018, Ricardo Carrillo Cruz <ricarril@redhat.com>
# (c) 2018, Yanis Guenane <yguenane@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action.cloud_base import ActionModule as _ActionModule


class ActionModule(_ActionModule):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        return result
