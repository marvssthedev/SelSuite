#!/bin/bash

# Setup dependencies that are not covered by pip

root="/home/$USER/Code/SelSuite"
unamestr=$(uname)
if [[ "$unamestr" == 'Linux' ]]; then
    wget="/usr/bin/wget"
    unzip="/usr/bin/unzip"
elif [[ "$unamestr" == 'FreeBSD' ]]; then
    wget="/usr/local/bin/wget"
    unzip="/usr/local/bin/unzip"
fi

cd $root
rm -rf "drivers" "server"
mkdir -p "drivers"
mkdir -p "server"

# A fail-safe so that we don't accidentally delete existing screenshots
if [ ! -d "screenshots" ]; then
    mkdir -p "screenshots"
fi

cd drivers
wget https://chromedriver.storage.googleapis.com/2.28/chromedriver_linux64.zip
unzip chromedriver_*.zip
rm chromedriver_*.zip

wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz
tar zxf geckodriver-*.tar.gz
rm geckodriver-*.tar.gz
cd ..

cd server
wget http://selenium-release.storage.googleapis.com/3.3/selenium-server-standalone-3.3.1.jar
cd ..

