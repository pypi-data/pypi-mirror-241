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

"""proxmox_backup_removable_datastore Utils module
"""

import subprocess
import datetime

def restart_proxmox_backup():
    """Restart proxmox backup services to unlock device"""
    subprocess.run(['systemctl restart proxmox-backup proxmox-backup-proxy'], check=False)

def last_sunday_of_month(date):
    """Return the date of the last sunday of the month."""
    month = date.month
    year = date.year

    # Définit le numéro de mois suivant
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    # Récupère la date du premier jour du mois suivant
    date = datetime.datetime(year, month, 1)

    # Ajoute à la date le nombre de jour pour atteindre le premier dimanche du mois
    # suivant et soustrait une semaine pour obtenir le dernier dimanche du mois en cours
    date = date + datetime.timedelta(days=6-date.weekday()) - datetime.timedelta(days=7)

    return date
