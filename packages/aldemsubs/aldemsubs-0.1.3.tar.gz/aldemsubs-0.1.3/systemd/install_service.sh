#!/usr/bin/env bash

echo "This script asks for root privileges. Please read it before continuing. It's not long, I promise.
"
echo "Continue? [y|N]"
read -n 1 answer
[[ $answer =~ ^[yY]$ ]] || { echo "Aborting!"; exit 1; }
echo ""

service=\
"[Unit]
Description=Update Youtube subscriptions with aldemsubs
RefuseManualStart=no
RefuseManualStop=no
 
[Service]
Type=oneshot
User=$(whoami)
ExecStart=python -m aldemsubs -ud"

echo "$service" > /tmp/aldemsubs.service
sudo chown root:root /tmp/aldemsubs.service || exit $?
sudo cp /tmp/aldemsubs.service /lib/systemd/system/
sudo rm /tmp/aldemsubs.service
