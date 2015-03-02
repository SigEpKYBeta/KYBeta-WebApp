# Sigma Phi Epsilon - KY Beta
## Web Application

### Installation
Clone this repository onto your local machine. 
```sh
$ git clone https://github.com/SigEpKYBeta/WebApp.git
```
Start the virtual machine with vagrant and then ssh into it
```sh
$ vagrant up
$ vagrant ssh
```
Source your virtual enviorment after sshing into it
```sh
$ source /vagrant/bin/activate
```
You are now set up for development.

### Running the Server

```sh
$ cd \vagrant\SigEp_App
$ python manage.py runserver 0.0.0.0:8000
```
With the server still running, you now have access to the server from your browser
by accessing 127.0.0.1:4567

