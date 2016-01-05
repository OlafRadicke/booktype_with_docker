#!/bin/bash

echo "DJANGO_SETTINGS_MODULE:"
echo $DJANGO_SETTINGS_MODULE

# Initialise Booktype
source ${instancename}/booktype.env
django-admin.py syncdb --noinput
django-admin.py migrate
django-admin.py createsuperuser
#django-admin.py createsuperuser --username='sysadmin' --email='sysadmin@okfn.org' --noinput

# This has to be done every time you want to start a server
#cd /docker_booktype
source /docker_booktype/bin/activate
source ${instancename}/booktype.env
django-admin.py runserver 0.0.0.0:8080
