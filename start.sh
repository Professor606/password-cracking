#!/bin/bash


figlet PASSWORD

sleep 1

figlet CRACKING

sleep 1

echo "ENTER THE NAME : "
read name

sleep 1

# Run the Python script and save the output with a timestamped filename
python3 python.py "$name" > "${name}$(date +%S).txt"
