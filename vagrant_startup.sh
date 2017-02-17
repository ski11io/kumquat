#/bin/bash

# apply migrations if necessary
echo "applying migrations"
/vagrant/manage.py migrate

# start development server
echo "starting dev server"
/vagrant/manage.py runserver 0.0.0.0:8000 &
