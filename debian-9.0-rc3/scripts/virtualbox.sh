#apt-get -y install virtualbox-guest-utils
sudo apt-get -y install wget make gcc
#wget http://download.virtualbox.org/virtualbox/5.0.22/VBoxGuestAdditions_5.0.22.iso
wget http://download.virtualbox.org/virtualbox/5.1.18/VBoxGuestAdditions_5.1.18.iso
sudo mkdir /media/VBoxGuestAdditions
#sudo mount -o loop,ro VBoxGuestAdditions_5.0.22.iso /media/VBoxGuestAdditions
sudo mount -o loop,ro VBoxGuestAdditions_5.1.18.iso /media/VBoxGuestAdditions
sudo sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
# rm VBoxGuestAdditions_5.0.22.iso
rm VBoxGuestAdditions_5.1.18.iso
sudo umount -l /media/VBoxGuestAdditions
sudo rmdir /media/VBoxGuestAdditions
