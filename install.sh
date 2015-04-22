# Install packages for development
echo "Updating Apt"
sudo apt-get update -y > /dev/null

echo "Installing python dependencies"
sudo apt-get install -y build-essential python python-setuptools python3-pip python-dev > /dev/null

echo "Installing Curl"
sudo apt-get install -y curl > /dev/null

echo "Installing git. DO NOT COMMIT ON VM"
sudo apt-get install -y git > /dev/null

#install PostgreSQL
echo "Installing and setting up PostgreSQL"
sudo apt-get install -y postgresql postgresql-contrib libpq-dev > /dev/null

sudo cat << EOF | su - postgres -c psql
-- Create the database user:
CREATE USER admin WITH PASSWORD 'password';

-- Create the database:
CREATE DATABASE sigeptest WITH OWNER=admin

EOF

# install and setup a virtualenv
echo "Installing Python virtualenv"
sudo pip3 install virtualenv
echo "Setting up virutalenv at /vagrant/SigEpDev"
cd /vagrant
sudo virtualenv SigEpDev > /dev/null
source /vagrant/SigEpDev/bin/activate > /dev/null

# install pip packages
echo "Installing Django 1.7 "
pip install Django > /dev/null
echo "Installing PostgreSQL connectors"
pip install psycopg2 > /dev/null

# install node and npm and update
echo "Installing Node.js and NPM"
sudo curl -sL https://deb.nodesource.com/setup | sudo bash - > /dev/null
sudo apt-get install -y nodejs > /dev/null
sudo npm install npm -g > /dev/null

sudo apt-get clean > /dev/null

# install bower
echo "Installing bower"
sudo npm install -g bower > /dev/null

# install SASS
echo "Installing SASS"
sudo gem install sass > /dev/null

echo "Installing bower packages"
bower install > /dev/null

echo "Trying to start server"

#cd source/
# python manage.py runserver 0.0.0.0:8000 &
# echo "Server running on 0.0.0.0:8000 (Access with localhost:4567)"
