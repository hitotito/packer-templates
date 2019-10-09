date > /etc/vagrant_box_build_time

sudo useradd -d /home/vagrant vagrant

mkdir -p /home/vagrant/.ssh
chown -R vagrant /home/vagrant/.ssh
chmod -R go-rwsx /home/vagrant/.ssh

exit 0
