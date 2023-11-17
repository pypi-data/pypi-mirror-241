#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This file is part of proxmox_backup_removable_datastore.

# proxmox_backup_removable_datastore is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.

# proxmox_backup_removable_datastore is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# proxmox_backup_removable_datastore. If not, see
# <https://www.gnu.org/licenses/gpl-3.0.txt>.

"""proxmox_backup_removable_datastore Datastore module
"""


import json
import subprocess
import sys
import datetime

from proxmox_backup_removable_datastore.models.utils import (
    restart_proxmox_backup,
    last_sunday_of_month
)

class Datastore():
    """Class representing a datastore
    """

    def __init__(self,
                 datastore_name,
                 datastore_path,
                 datastore_maintenance_mode = "online",
                 datastore_comment = None,
                 datastore_notify_user = None,
                 datastore_gc_schedule = None,
                 datastore_prune_schedule = None,
                 datastore_keep_last = None,
                 datastore_keep_daily = None,
                 datastore_keep_weekly = None,
                 datastore_keep_monthly = None,
                 datastore_keep_yearly = None,
                 **_
                ):
        """_summary_

        :param datastore_name: Name of the datastore
        :type datastore_name: str
        :param datastore_path: Path to the datastore
        :type datastore_path: str
        :param datastore_maintenance_mode: Maintenance mode on the datastore, defaults to "online"
        :type datastore_maintenance_mode: str, optional
        :param datastore_comment: Comment of the datastore, defaults to None
        :type datastore_comment: str, optional
        :param datastore_notify_user: User to notify, defaults to None
        :type datastore_notify_user: str, optional
        :param datastore_gc_schedule: Garbage schedule on datastore, defaults to None
        :type datastore_gc_schedule: str, optional
        :param datastore_prune_schedule: Prune schedule on datastore, defaults to None
        :type datastore_prune_schedule: str, optional
        :param datastore_keep_last: Number of last backup to keep, defaults to None
        :type datastore_keep_last: int, optional
        :param datastore_keep_daily: Number of daily backup to keep, defaults to None
        :type datastore_keep_daily: int, optional
        :param datastore_keep_weekly: Number of weekly backup to keep, defaults to None
        :type datastore_keep_weekly: int, optional
        :param datastore_keep_monthly: Number of monthly backup to keep, defaults to None
        :type datastore_keep_monthly: int, optional
        :param datastore_keep_yearly: Number of yearly backup to keep, defaults to None
        :type datastore_keep_yearly: int, optional
        """

        self._name = datastore_name
        self._path = datastore_path
        self._maintenance_mode = datastore_maintenance_mode
        self._comment = datastore_comment
        self._notify_user = datastore_notify_user
        self._gc_schedule = datastore_gc_schedule
        self._prune_schedule = datastore_prune_schedule
        self._keep_last = datastore_keep_last
        self._keep_daily = datastore_keep_daily
        self._keep_weekly = datastore_keep_weekly
        self._keep_monthly = datastore_keep_monthly
        self._keep_yearly = datastore_keep_yearly

    @property
    def name(self):
        """Get the name of the datastore

        :return: _name
        :rtype: str
        """
        return self._name

    @property
    def path(self):
        """Get the path to the datastore

        :return: _path
        :rtype: str
        """
        return self._path

    @property
    def maintenance_mode(self):
        """Get the maintenance mode on the datastore

        :return: _maintenance_mode
        :rtype: str
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, value):
        """Set the maintenance mode on the datastore

        :param value: Set the datastore mode. Accept only to value : "online", "offline"
        :type value: str
        """
        if value in ['online', 'offline']:
            self._maintenance_mode = value
        else:
            print('Datastore maintenance mode should be \'online\' or \'offline\'')
            sys.exit(1)

    @property
    def comment(self):
        """Get comment of the datastore

        :return: _comment
        :rtype: str
        """
        return self._comment

    @property
    def notify_user(self):
        """Get notify user

        :return: _notify_user
        :rtype: str
        """
        return self._notify_user

    @property
    def gc_schedule(self):
        """Get garbage schedule define on datastore

        :return: _gc_schedule
        :rtype: str
        """
        return self._gc_schedule

    @property
    def prune_schedule(self):
        """Get prune schedule define on datastore

        :return: _prune_schedule
        :rtype: str
        """
        return self._prune_schedule

    @property
    def keep_last(self):
        """Get number of last backup to keep

        :return: _keep_last
        :rtype: int
        """
        return self._keep_last

    @property
    def keep_daily(self):
        """Get number of daily backup to keep

        :return: _keep_daily
        :rtype: int
        """
        return self._keep_daily

    @property
    def keep_weekly(self):
        """Get number of weekly backup to keep

        :return: _keep_weekly
        :rtype: int
        """
        return self._keep_weekly

    @property
    def keep_monthly(self):
        """Get number of monthly backup to keep

        :return: _keep_monthly
        :rtype: int
        """
        return self._keep_monthly

    @property
    def keep_yearly(self):
        """Get number of yearly backup to keep

        :return: _keep_yearly
        :rtype: int
        """
        return self._keep_yearly

    def garbage(self):
        """Run garbage job on datastore
        """
        subprocess.run(['proxmox-backup-manager',
                        'garbage-collection',
                        'start',
                        self.name],
                        check=False
                      )

    def enable(self):
        """Enable datastore
        """
        if self.maintenance_mode == 'offline':
            subprocess.run(['proxmox-backup-manager',
                            'datastore',
                            'update',
                            self.name,
                            '--delete',
                            'maintenance-mode'],
                            check=False
                          )
            self.maintenance_mode = 'online'
            print('Datastore is now online')
        else:
            print('Datastore is already online')

    def disable(self):
        """Disable datastore
        """
        if self.maintenance_mode == 'online':
            subprocess.run(['proxmox-backup-manager',
                            'datastore',
                            'update',
                            self.name,
                            '--maintenance-mode',
                            'offline'],
                            check=False
                          )
            self.maintenance_mode = 'offline'
            print('Datastore is now offline')
        else:
            print('Datastore is already offline')

    def eject(self, period):
        """Eject RDX tape based on the period defined."""
        date = datetime.datetime.today()

        if period == 'daily':
            restart_proxmox_backup()
            subprocess.run(['eject', self.path], check=False)
            status = 'RDX tape ejected'

        elif period == 'weekly':
            if date.weekday() == 6:
                restart_proxmox_backup()
                subprocess.run(['eject', self.path], check=False)
                status = 'RDX tape ejected'
            else:
                status = 'RDX tape not ejected'

        elif period == 'monthly':
            if date.strftime("%d-%m-Y") == last_sunday_of_month(date).strftime("%d-%m-Y"):
                restart_proxmox_backup()
                subprocess.run(['eject', self.path], check=False)
                status = 'RDX tape ejected'
            else:
                status = 'RDX tape not ejected'

        else:
            status = 'RDX tape not ejected'
        return status

    @staticmethod
    def get(datastore_name):
        """Return Datastore object based on proxmox datastore name

        :param datastore_name: Datastore name
        :type datastore_name: str
        :return: Datastore or NoneType object
        :rtype: Datastore / NoneType
        """
        process = subprocess.run(['proxmox-backup-manager',
                                  'datastore',
                                  'list',
                                  '--output-format',
                                  'json'],
                                  capture_output=True,
                                  check=False
                                )
        json_result = json.loads(process.stdout.decode())

        for datastore_json in json_result:
            if datastore_json['name'] == datastore_name:

                # Création d'un dictionnaire vide contenant les
                # attribut nécessaire à la création d'une instance
                # de la classe Datastore.
                __attr = {}
                for key, value in datastore_json.items():
                    __attr.update({f'datastore_{key.replace("-", "_")}': value})

                datastore = Datastore(**__attr)
                return datastore

        return None
