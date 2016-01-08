#!/bin/bash

echo "DJANGO_SETTINGS_MODULE:"
echo $DJANGO_SETTINGS_MODULE

cd /${instancename}/
/${instancename}/manage.py
runserver 0.0.0.0:8080
