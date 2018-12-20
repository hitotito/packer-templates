# TODO - This is virtualbox version independent.  We should work on building different version
#apt-get -y install virtualbox-guest-utils
sudo apt-get -y install wget make gcc
wget https://download.virtualbox.org/virtualbox/5.2.8/VBoxGuestAdditions_5.2.8.iso
sudo mkdir /media/VBoxGuestAdditions
sudo mount -o loop,ro VBoxGuestAdditions_5.2.8.iso /media/VBoxGuestAdditions
sudo sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
rm VBoxGuestAdditions_5.2.8.iso
sudo umount -l /media/VBoxGuestAdditions
sudo rmdir /media/VBoxGuestAdditions
