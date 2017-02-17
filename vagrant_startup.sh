#/bin/bash

# apply migrations if necessary
echo "applying migrations"
/vagrant/manage.py migrate

# start development server
echo "starting dev server"
/vagrant/manage.py runserver 0.0.0.0:8000 &

echo "adding admin user"
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'qwe123')" | python /vagrant/manage.py shell

echo "------------------------------------------"
echo "everything is fine... -> check http://127.0.0.1:8000"
