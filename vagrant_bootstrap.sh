#/bin/bash

echo export LC_ALL=C >> ~/.bashrc
echo export LC_ALL=C >> /home/ubuntu/.bashrc

apt-get update

#predefine answers for mysql-server installation prompts
debconf-set-selections <<< 'mysql-server mysql-server/root_password password qwe123'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password qwe123'

#install os dependencies
apt-get install -y python-pip mysql-server libmysqlclient-dev libffi-dev libssl-dev

#update pip
pip install --upgrade pip

#install required pip components
pip install -r /vagrant/req.txt

#check if sqlite db is present and delete it to get a fresh start
if [ -f /vagrant/db.sqlite3 ]; then
   echo "Removing existing sqlitedb..."
   rm /vagrant/db.sqlite3
