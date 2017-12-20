date > /etc/vagrant_box_build_time

sudo useradd -Dd /home/vagrant vagrant

mkdir /home/vagrant/.ssh
wget --no-check-certificate \
    'https://raw.githubusercontent.com/hitotito/pubkey/master/vagrant/id_rsa.pub' \
    -O /home/vagrant/.ssh/authorized_keys
chown -R vagrant /home/vagrant/.ssh
chmod -R go-rwsx /home/vagrant/.ssh

sudo mkdir -p /root/.ssh/
sudo cp /home/vagrant/.ssh/authorized_keys /root/.ssh/authorized_keys

exit 0
