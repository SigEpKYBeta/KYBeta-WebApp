# # Install packages for development
apt-get update -y
apt-get install -y python3-pip

# install and setup a virtualenv
pip3 install virtualenv
virtualenv /vagrant
source /vagrant/bin/activate
cd /vagrant

# install
pip install Django

#cleanup
apt-get clean

