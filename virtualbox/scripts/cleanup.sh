apt-get -y autoremove
apt-get -y clean

echo "cleaning up guest additions"
rm -rf /home/vagrant/VBoxGuestAdditions_*.iso /home/vagrant/VBoxGuestAdditions_*.iso.?

echo "cleaning up dhcp leases"
rm /var/lib/dhcp/*

echo "cleaning up udev rules"
rm -f /etc/udev/rules.d/70-persistent-net.rules
mkdir /etc/udev/rules.d/70-persistent-net.rules
rm -rf /dev/.udev/
rm -f /lib/udev/rules.d/75-persistent-net-generator.rules
