# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  
  # Use the ubuntu 14.04 64-bit OS
  config.vm.box = "ubuntu/trusty64"

  # Setup proxy using the Vagrant pronxyconf plugin
  # if there is no proxy present then the proxy should
  # not be set
  if Vagrant.has_plugin?("vagrant-proxyconf")
      config.proxy.http     = "http://10.10.9.100:8080"
      config.proxy.https    = "http://10.10.9.100:8080"
      config.proxy.no_proxy = "localhost,127.0.0.1"
  end

  # Forward a port from the guest to the host, which allows for outside	
  # computers to access the VM, whereas host only networking does not.
  config.vm.network "forwarded_port", guest: 4567, host: 8000
  # Provision the VM with a shell script
  config.vm.provision :shell, :path => "install.sh"
end
