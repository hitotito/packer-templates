date > /etc/vagrant_box_build_time

sudo useradd -Dd /home/vagrant vagrant

mkdir /home/vagrant/.ssh
chown -R vagrant /home/vagrant/.ssh
chmod -R go-rwsx /home/vagrant/.ssh

exit 0
