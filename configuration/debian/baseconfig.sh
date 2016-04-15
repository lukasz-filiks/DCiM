#this script should be executed after fresh debian installation on beaglebone

#should be run as root
sudo su

#update time on the beagle
ntpdate pool.ntp.org

#update APT repository
apt-get update
apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y

#install GPIO library
pip install Adafruit_BBIO

