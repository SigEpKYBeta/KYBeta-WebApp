DBPASS=1111901

# Install packages for development
echo "Updating Apt"
apt-get update -y > /dev/null

echo "Installing python-pip"
apt-get install -y python3-pip > /dev/null

echo "Installing Curl"
apt-get install -y curl > /dev/null

echo "Installing git. DO NOT COMMIT ON VM"
apt-get install -y git > /dev/null

#install and setup mysql
echo "Installing and setting up MySQL"
apt-get install -y debconf-utils > /dev/null
debconf-set-selections <<< 'mysql-server mysql-server/root_password password $DBPASS'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password $DBPASS'
apt-get install -y mysql-server > /dev/null
apt-get install -y libmysqlclient-dev > /dev/null

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
echo "Installing Python MySQL Connectors"
pip install MySQL-python > /dev/null

# install node and npm and update
echo "Installing Node.js and NPM"
curl -sL https://deb.nodesource.com/setup | sudo bash - > /dev/null
apt-get install -y nodejs > /dev/null
npm install npm -g > /dev/null

# install bower
echo "Installing bower"
npm install -g bower > /dev/null

#cleanup
echo "Cleaning up"
apt-get clean > /dev/null

