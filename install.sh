# # Install packages for development
apt-get update -y
apt-get install -y python3-pip curl

# install and setup a virtualenv
pip3 install virtualenv
virtualenv /vagrant
source /vagrant/bin/activate
cd /vagrant

# install
pip install Django

# install node and npm and update
curl -sL https://deb.nodesource.com/setup | sudo bash -
apt-get install -y nodejs
npm install npm -g

# install bower
npm install -g bower

# install bower packages
cd /vagrant

#cleanup
apt-get clean

