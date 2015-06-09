# Install packages for development
echo "Updating Apt"
apt-get update -y > /dev/null

echo "Installing python dependencies"
apt-get install -y build-essential python python-setuptools python3-pip python-dev > /dev/null

echo "Installing Curl"
apt-get install -y curl > /dev/null

echo "Installing git. DO NOT COMMIT ON VM"
apt-get install -y git > /dev/null

#install PostgreSQL
echo "Installing and setting up PostgreSQL"
apt-get install -y postgresql postgresql-contrib libpq-dev > /dev/null

cat << EOF | su - postgres -c psql
-- Create the database user:
CREATE USER admin WITH PASSWORD 'password';

-- Create the database:
CREATE DATABASE sigeptest WITH OWNER=admin

EOF

# install and setup a virtualenv
echo "Installing Python virtualenv"
pip3 install virtualenv
echo "Setting up virutalenv at /vagrant/SigEpDev"
cd /vagrant
virtualenv SigEpDev > /dev/null
source /vagrant/SigEpDev/bin/activate > /dev/null

# install pip packages
echo "Installing Django 1.8.2 "
pip install Django==1.8.2 > /dev/null
echo "Installing PostgreSQL connectors"
pip install psycopg2 > /dev/null

# install node and npm and update
echo "Installing Node.js and NPM"
curl -sL https://deb.nodesource.com/setup | sudo bash - > /dev/null
apt-get install -y nodejs > /dev/null
npm install npm -g > /dev/null

apt-get clean > /dev/null

export STATE="dev"
export DB_USER="admin"
export DB_PASS="password"
export DB_NAME="sigeptest"

echo "export STATE=dev" >> /home/vagrant/.bashrc
echo "export DB_USER=admin" >> /home/vagrant/.bashrc
echo "export DB_PASS=password" >> /home/vagrant/.bashrc
echo "export DB_NAME=sigeptest" >> /home/vagrant/.bashrc

echo "Trying to start server"
cd source/
python manage.py runserver 0.0.0.0:8000 &
echo "Server running on 0.0.0.0:8000 (Access with localhost:4567)"
