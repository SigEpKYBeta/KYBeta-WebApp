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
apt-get install -y postgresql postgresql-contrib libpq-dev

cat << EOF | su - postgres -c psql
-- Create the database user:
CREATE USER admin WITH PASSWORD 'password';

-- Create the database:
CREATE DATABASE sigeptest WITH OWNER=admin

EOF

# install and setup a virtualenv
echo "Installing Python virtualenv"
pip3 install virtualenv > /dev/null
echo "Setting up virutalenv at /vagrant"
virtualenv /vagrant > /dev/null
source /vagrant/bin/activate
cd /vagrant

# install pip packages
echo "Installing Django 1.7 "
pip install Django > /dev/null
echo "Installing PostgreSQL connectors"
pip install psycopg2

# install node and npm and update
echo "Installing Node.js and NPM"
curl -sL https://deb.nodesource.com/setup | sudo bash - > /dev/null
apt-get install -y nodejs > /dev/null
npm install npm -g > /dev/null

# install bower
echo "Installing bower"
npm install -g bower > /dev/null

# install SASS
gem install sass

#cleanup
echo "Cleaning up"
apt-get clean > /dev/null

