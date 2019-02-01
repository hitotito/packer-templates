# TODO - This is virtualbox version independent.  We should work on building different version
#        In order to do this, we will have to figure out a way to spin up different build environment
#        for each virtualbox version
#apt-get -y install virtualbox-guest-utils
sudo apt-get -y install wget make gcc
wget https://download.virtualbox.org/virtualbox/6.0.4/VBoxGuestAdditions_6.0.4.iso
sudo mkdir /media/VBoxGuestAdditions
sudo mount -o loop,ro VBoxGuestAdditions_6.0.4.iso /media/VBoxGuestAdditions
sudo sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
rm VBoxGuestAdditions_6.0.4.iso
sudo umount -l /media/VBoxGuestAdditions
sudo rmdir /media/VBoxGuestAdditions
