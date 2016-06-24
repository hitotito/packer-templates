#apt-get -y install virtualbox-guest-utils
sudo apt-get -y install wget make gcc
wget http://download.virtualbox.org/virtualbox/5.0.22/VBoxGuestAdditions_5.0.22.iso
sudo mkdir /media/VBoxGuestAdditions
sudo mount -o loop,ro VBoxGuestAdditions_5.0.22.iso /media/VBoxGuestAdditions
sudo sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
rm VBoxGuestAdditions_5.0.22.iso
sudo umount /media/VBoxGuestAdditions
sudo rmdir /media/VBoxGuestAdditions
sudo rm VBoxGuestAdditions_5.0.22.iso
