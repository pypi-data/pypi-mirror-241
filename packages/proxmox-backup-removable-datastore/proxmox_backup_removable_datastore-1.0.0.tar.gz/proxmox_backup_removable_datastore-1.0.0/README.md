# proxmox-backup-removable-datastore

This program launches the jobs configured in Proxmox Backup Server (Sync, Prune, Garbage) and ejects the removable device at the end of the process. It synchronises the PBX datastore on a removable device such as an RDX tape.

## Requirements

* `proxmox-backup-manager ≥ 3.0`
* `python ≥ 3.9`
* `pip`

### For Debian System

```sh
sudo apt install python3 python3-pip
```

## Install

```sh
python3 -m pip install proxmox-backup-removable-storage
```

## Usage


## Howto

You can find howto to configure removable storage, tasks, and more on the `./docs` directory.

## Licence

GPL-3.0-or-later