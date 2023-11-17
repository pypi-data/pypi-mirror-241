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

"""proxmox_backup_removable_datastore Prune module
"""


import json
import subprocess

class PruneJob():
    """Class representing a prune job
    """

    def __init__(self,
                 prunejob_id,
                 prunejob_store,
                 prunejob_ns=None,
                 prunejob_comment=None,
                 prunejob_disable=False,
                 prunejob_keep_last=None,
                 prunejob_keep_daily=None,
                 prunejob_keep_weekly=None,
                 prunejob_keep_monthly=None,
                 prunejob_keep_yearly=None,
                 prunejob_schedule=None
                ):
        """Constructor of PruneJob object

        :param prunejob_id: ID of the prune job
        :type prunejob_id: str
        :param prunejob_store: Datastore name where is applied the prune job
        :type prunejob_store: str
        :param prunejob_ns: Datastore name where is applied the prune job, defaults to None
        :type prunejob_ns: str, optional
        :param prunejob_comment: Comment of the prune job, defaults to None
        :type prunejob_comment: str, optional
        :param prunejob_disable: Define if schedule is disable, defaults to False
        :type prunejob_disable: bool, optional
        :param prunejob_keep_last: Number of last backup to keep, defaults to None
        :type prunejob_keep_last: int, optional
        :param prunejob_keep_daily: Number of daily backup to keep, defaults to None
        :type prunejob_keep_daily: int, optional
        :param prunejob_keep_weekly: Number of weekly backup to keep, defaults to None
        :type prunejob_keep_weekly: int, optional
        :param prunejob_keep_monthly: Number of monthly backup to keep, defaults to None
        :type prunejob_keep_monthly: int, optional
        :param prunejob_keep_yearly: Number of yearly backup to keep, defaults to None
        :type prunejob_keep_yearly: int, optional
        :param prunejob_schedule: Schedule of the prune job, defaults to None
        :type prunejob_schedule: str, optional
        """

        self._id = prunejob_id
        self._store = prunejob_store
        self._ns = prunejob_ns
        self._comment = prunejob_comment
        self._disable = prunejob_disable
        self._keep_last = prunejob_keep_last
        self._keep_daily = prunejob_keep_daily
        self._keep_weekly = prunejob_keep_weekly
        self._keep_monthly = prunejob_keep_monthly
        self._keep_yearly = prunejob_keep_yearly
        self._schedule = prunejob_schedule

    @property
    def id(self):
        """Get prune job id

        :return: _id
        :rtype: str
        """
        return self._id

    @property
    def store(self):
        """Get prune job datastore

        :return: _store
        :rtype: str
        """
        return self._store

    @property
    def ns(self):
        """Get prune job namespace

        :return: _ns
        :rtype: str
        """
        return self._ns

    @property
    def comment(self):
        """Get comment

        :return: _comment
        :rtype: str
        """
        return self._comment

    @property
    def disable(self):
        """Get status of schedule

        :return: _disable
        :rtype: bool
        """
        return self._disable

    @property
    def keep_last(self):
        """Get number of last backup to keep

        :return: _prunejob_keep_last
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

    @property
    def schedule(self):
        """Get prune job schedule

        :return: _schedule
        :rtype: int
        """
        return self._schedule


    def run(self):
        """Run the prune job
        """
        subprocess.run(['proxmox-backup-manager',
                        'prune-job',
                        'run',
                        self.id],
                        check=False
                      )

    @staticmethod
    def get(prunejob_id):
        """Return PruneJob object based on proxmox prune_job id

        :param prunejob_id: Prune Job ID
        :type prunejob_id: str
        :return: PruneJob or NoneType object
        :rtype: PruneJob / NoneType
        """


        process = subprocess.run(['proxmox-backup-manager',
                                  'prune-job',
                                  'list',
                                  '--output-format',
                                  'json'],
                                  capture_output=True,
                                  check=False
                                )

        json_result = json.loads(process.stdout.decode())

        for prunejob_json in json_result:
            if prunejob_json['id'] == prunejob_id:

                # Création d'un dictionnaire vide contenant les
                # attribut nécessaire à la création d'une instance
                # de la classe PruneJob.
                __attr = {}
                for key, value in prunejob_json.items():
                    __attr.update({f'prunejob_{key.replace("-", "_")}': value})

                prunejob = PruneJob(**__attr)
                return prunejob

        return None
