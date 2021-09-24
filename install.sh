#!/bin/bash
echo "========================================================="
echo "==!! Simpletrons : Simplify Opentrons API 1 for OT-1!!=="
echo "========================================================="
echo "============="
#Detect Ubuntu or Window Version or Max OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update && upgrade -y
	sudo apt install python git -y
	sudo pip3 install opentrons==2.5.2
	sudo pip3 install curse
	sudo pip3 install mysql-connector-python 
elif [[ "$OSTYPE" == "darwin"* ]]; then
        pip install opentrons==2.5.2
        pip install cursed
        pip install mysql-connector-python 
elif [[ "$OSTYPE" == "cygwin" ]]; then
        pip install opentrons==2.5.2
        pip install windows-curses
        pip install mysql-connector-python 
elif [[ "$OSTYPE" == "msys" ]]; then
        pip install opentrons==2.5.2
        pip install windows-curses
        pip install mysql-connector-python 
elif [[ "$OSTYPE" == "win32" ]]; then
        pip install opentrons==2.5.2
        pip install windows-curses
        pip install mysql-connector-python 
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        pkg apt update && upgrade -y
        pkg install python3.7 git -y
	python3 pip install opentrons==2.5.2
	python3 pip install curse
	python3 pip install mysql-connector-python 
fi