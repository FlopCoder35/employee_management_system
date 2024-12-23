#!/usr/bin/env bash
set -o errexit
.venv\Scripts\activate 
pip install -r requirements.txt

# Update path to manage.py if it's in a subdirectory
python Officemanage/manage.py collectstatic --no-input
python Officemanage/manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python Officemanage/manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
