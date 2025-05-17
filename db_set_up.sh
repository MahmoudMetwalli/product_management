#!/usr/bin/bash

sudo apt update
sudo apt install postgresql
sudo -u postgres psql -c "CREATE USER mahmoud WITH PASSWORD 'simple#system567';" \
-c "CREATE DATABASE chat OWNER mahmoud;" \
-c "GRANT ALL PRIVILEGES ON DATABASE chat TO mahmoud;"
sudo service postgresql restart
