# Install packages for development
apt-get update -y
apt-get install -y build-essential python python-dev python-setuptools python-pip

# install Django 
pip install Django

#cleanup
apt-get clean
