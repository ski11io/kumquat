#/bin/bash

echo export LC_ALL=C >> ~/.bashrc
echo export LC_ALL=C >> /home/ubuntu/.bashrc
apt-get update

debconf-set-selections <<< 'mysql-server mysql-server/root_password password qwe123'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password qwe123'

apt-get install -y python-pip mysql-server libmysqlclient-dev libffi-dev libssl-dev

pip install --upgrade pip

pip install -r /vagrant/req.txt
