#/bin/bash

echo export LC_ALL=C >> ~/.bashrc
echo export LC_ALL=C >> /home/ubuntu/.bashrc

apt-get install mysql-server nginx libmysqlclient-dev
