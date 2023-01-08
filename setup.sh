#!/bin/bash
 
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
 
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
 
apt update -y
 
apt install -y google-chrome-stable
 
apt install -yqq unzip
 
apt install -y python3-pip
 
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
 
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
 
pip3 install --upgrade pip
 
pip3 install selenium
 
pip3 install pandas
 
pip3 install matplotlib
