# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "master" do |m|
        m.vm.box = "ubuntu/focal64"
        m.vm.hostname = "docker.localhost"
        m.vm.network "private_network", ip: "192.168.56.0"
        m.vm.provision "docker"
        m.vm.provider :virtualbox do |vb|
                vb.customize [ 'modifyvm', :id, '--memory', '4000' ]
                vb.customize [ 'modifyvm', :id, '--cpus', '1' ]
                vb.customize [ 'modifyvm', :id, '--name', 'docker' ]
        end
  end
end

