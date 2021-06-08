#!/bin/bash
echo "========================================================="
echo "==!! Simpletrons : Simplify Opentrons API 1 for OT-1!!=="
echo "========================================================="
echo "============="
#Detect Ubuntu or Window Version


#Ubuntu Install 
sudo apt update && upgrade -y
sudo apt install python git -y
sudo python3 pip install opentrons==2.5.2
sudo python3 pip install curse

#Window Bash/Install