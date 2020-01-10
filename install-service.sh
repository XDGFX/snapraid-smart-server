#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

cp smartserver.service /etc/systemd/system/
chown root:root /etc/systemd/system/smartserver.service
chmod 644 /etc/systemd/system/smartserver.service

echo "~ Successfully installed service"
echo "~ Attempting to enable"

systemctl enable smartserver.service

echo "~ Successfully enabled service"
echo "~ Attempting to start service"

systemctl start smartserver.service

systemctl status smartserver.service