# Kumquat

Small scale virtual hosting portal.

## Features

- Web VHost management (including support for SSL Certificates)
- MySQL Database management
- FTP Users
- No complicated reseller/permission system (single user model)
- Relatively agnostic to server software (built for SmartOS Zones with apache from pkgsrc, but support for nginx would be just one template change and a setting away)
- (optional) per VHost ZFS filesystem allows fine grained snapshots and backups

## Vagrant dev box

WARNING: still in developement, atm just the frontend works login etc are currently not possible

Tested with

 - Vagrant 1.9.1
 - Virtualbox 5.1.14


 simply run this at the base of your repo

    vagrant up


if you do not see any errors kumquat should running at http://127.0.0.1:8000

create a superuseraccount with

    vagrant ssh
    /vagrant/manage.py createsuperuser --username=admin
