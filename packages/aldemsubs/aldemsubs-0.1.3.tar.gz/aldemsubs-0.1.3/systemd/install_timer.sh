#!/usr/bin/env bash

echo "This script asks for root privileges. Please read it before continuing. It's not long, I promise.
"
echo "Continue? [y|N]"
read -n 1 answer
[[ $answer =~ ^[yY]$ ]] || { echo "Aborting!"; exit 1; }
echo ""

timer=\
"[Unit]
Description=Update Youtube subscriptions with aldemsubs
RefuseManualStart=no
RefuseManualStop=no
 
[Timer]
Persistent=false
OnBootSec=5min
OnUnitActiveSec=1h 30min
Unit=aldemsubs.service
 
[Install]
WantedBy=timers.target"

temp="/tmp/aldemsubs.timer"
echo "$timer" > $temp
sudo chown root:root $temp || exit $?
sudo cp $temp /lib/systemd/system/
sudo rm $temp
