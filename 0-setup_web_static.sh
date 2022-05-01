#!/usr/bin/env bash
## Install web server - Nginx.
## -----------------------------
## Run sudo update.
sudo apt-get -y update
## Install nginx.
sudo apt-get -y install nginx
## sets up your web servers for the deployment of web_static. It must:
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
## sudo chown $USER:$USER /data/
sudo chown -R ubuntu:ubuntu /data/
## Create file index --> index.html to /data/web_static/releases/test/.
echo "Holberton School" > /data/web_static/releases/test/index.html
## line copy data path 1 --> path 2
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
## Service nginx - start.
sudo service nginx start
## adding line into location /etc/nginx/sites-available/default
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
## Restart service nginx
sudo service nginx restart