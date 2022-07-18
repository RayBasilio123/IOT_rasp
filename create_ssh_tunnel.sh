#!/bin/bash
createTunnel() {
  /usr/bin/ssh -i ray-julio.pem -NR localhost:$1:localhost:443 ubuntu@ec2-44-192-129-106.compute-1.amazonaws.com & 
  if [[ $? -eq 0 ]]; then
    echo Tunnel to jumpbox created successfully
  else
    echo An error occurred creating a tunnel to aws. RC was $?
  fi
}
/bin/pidof ssh
if [[ $? -ne 0 ]]; then
  echo Creating new tunnel connection
  createTunnel $1
fi
