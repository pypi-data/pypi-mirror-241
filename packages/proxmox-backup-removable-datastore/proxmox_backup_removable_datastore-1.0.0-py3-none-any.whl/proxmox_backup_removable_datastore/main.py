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

"""Main module of proxmox_backup_removable_datastore
"""

import argparse

from proxmox_backup_removable_datastore.models.datastore import Datastore
from proxmox_backup_removable_datastore.models.prunejob import PruneJob
from proxmox_backup_removable_datastore.models.syncjob import SyncJob

def script_argument():
    """
    Return arguments passed to the program
    """
    parser = argparse.ArgumentParser(
        prog='%(prog)s',
        description='Sync proxmox backup datastore to removable datastore',
        epilog='%(prog)s  Copyright (C) 2023 Mathieu Fruchet\n This program comes with \
        ABSOLUTELY NO WARRANTY; \n \
        This is free software, see the GNU General Public License for more details'
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')
    parser.add_argument('-d', '--datastore', dest='datastore', type=str, required=False,
                        help='Define the name of datastore')
    parser.add_argument('-s', '--sync-job', dest='sync_job_id', type=str, required=False,
                        help='Define ID of the sync job to start')
    parser.add_argument('-p', '--prune-job', dest='prune_job_id', type=str, required=False,
                        help='Define ID of the prune job to start')
    parser.add_argument('-g', '--garbage', action='store_true', dest="garbage", required=False,
                        help='Execute garbage job')
    parser.add_argument('-e', '--eject', dest='eject_period', type=str, default="never",
                        choices=["never", "daily", "weekly", "monthly"],
                        help='Define when the RDX tape removable device need to be ejected ')
    parser.parse_args()
    return parser.parse_args()

def main():
    """_summary_
    """
    args = script_argument()
    datastore_name = args.datastore
    syncjob_id = args.sync_job_id
    prunejob_id = args.prune_job_id
    eject_period = args.eject_period
    garbage = args.garbage

    datastore = Datastore.get(datastore_name)
    datastore.enable()

    if args.sync_job_id:
        syncjob = SyncJob.get(syncjob_id)
        syncjob.run()

    if args.prune_job_id:
        prunejob = PruneJob.get(prunejob_id)
        prunejob.run()

    if garbage:
        datastore.garbage()

    datastore.disable()

    datastore.eject(eject_period)

if __name__ == "__main__":
    main()
