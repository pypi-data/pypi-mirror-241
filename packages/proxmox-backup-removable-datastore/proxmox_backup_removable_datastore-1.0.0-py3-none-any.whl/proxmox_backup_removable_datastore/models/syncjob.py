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

"""proxmox_backup_removable_datastore Sync module
"""

import json
import subprocess

class SyncJob:
    """Class representing a sync job
    """

    def __init__(self,
                 syncjob_id,
                 syncjob_ns = None,
                 syncjob_owner = None,
                 syncjob_remote = None,
                 syncjob_remote_ns = None,
                 syncjob_remote_store = None,
                 syncjob_remove_vanished = False,
                 syncjob_store = None,
                 syncjob_transfer_last = None
                ):

        self._id = syncjob_id
        self._ns = syncjob_ns
        self._owner = syncjob_owner
        self._remote = syncjob_remote
        self._remote_ns = syncjob_remote_ns
        self._remote_store = syncjob_remote_store
        self._remove_vanished = syncjob_remove_vanished
        self._store = syncjob_store
        self._transfer_last = syncjob_transfer_last

    @property
    def id(self):
        """Get sync job id

        :return: _id
        :rtype: str
        """
        return self._id

    @property
    def ns(self):
        """Get sync job local namespace

        :return: _ns
        :rtype: str
        """
        return self._ns

    @property
    def store(self):
        """Get sync job local datastore

        :return: _store
        :rtype: str
        """
        return self._store

    @property
    def owner(self):
        """Get owner of local backup

        :return: _owner
        :rtype: str
        """
        return self._owner

    @property
    def remote(self):
        """Get sync job remote server

        :return: _remote
        :rtype: str
        """
        return self._remote

    @property
    def remote_ns(self):
        """Get sync job remote namespace

        :return: _remote_ns
        :rtype: str
        """
        return self._remote_ns

    @property
    def remote_store(self):
        """Get sync job remote datastore

        :return: _remote_store
        :rtype: str
        """
        return self._remote_store

    @property
    def remove_vanished(self):
        """Get sync job remove vanished

        :return: _remove_vanished
        :rtype: bool
        """
        return self._remove_vanished

    @property
    def transfer_last(self):
        """Get sync job transfer-last

        :return: _transfer_last
        :rtype: int
        """
        return self._transfer_last

    def run(self):
        """Run the sync job
        """
        subprocess.run(['proxmox-backup-manager',
                        'sync-job',
                        'run',
                        self.id],
                        check=False
                      )

    @staticmethod
    def get(syncjob_id):
        """Return PruneJob object based on proxmox sync_job id

        :param syncjob_id: Sync Job ID
        :type syncjob_id: str
        :return: SyncJob object or None
        :rtype: SyncJob / NoneType
        """

        process = subprocess.run(['proxmox-backup-manager',
                                  'sync-job',
                                  'list',
                                  '--output-format',
                                  'json'],
                                  capture_output=True,
                                  check=False
                                )
        json_result = json.loads(process.stdout.decode())

        for syncjob_json in json_result:
            if syncjob_json['id'] == syncjob_id:

                # Création d'un dictionnaire vide contenant les
                # attribut nécessaire à la création d'une instance
                # de la classe SyncJob.
                __attr = {}
                for key, value in syncjob_json.items():
                    __attr.update({f'syncjob_{key.replace("-", "_")}': value})

                syncjob = SyncJob(**__attr)
                return syncjob

        return None
