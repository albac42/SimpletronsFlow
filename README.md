Simpletrons Readme

# Simpletrons

Simplify Opentrons API 1 for OT-1


# How to get started

## Quick Install

For Linux (Ubuntu/Debian)
1. `sudo apt-get update && apt-get -y upgrade`
2. `git clone https://github.com/skydivercactus/simpletrons`
3. `cd simpletrons`
4. `sudo ./install.sh`

For Windows Based

1.  Download Git for Windows ([Download Latest Page](https://gitforwindows.org/)) ([Github v2.33.0 Download Link](https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.2/Git-2.33.0.2-64-bit.exe))
2.  Run the installer to install Git for Windows
3.  Download Python 3.x ([Download Latest Page](https://www.python.org/downloads/windows/)) ([Python 3.9.6 64 bit Download Link](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe))
4.  Ensure “Add Python 3.x to PATH” is checked before “Install Now”
5.  Start Github Bash
6.  Enter `git clone https://github.com/skydivercactus/simpletrons`
7.  Enter `cd simpletrons`
8.  Enter `./install.sh`

For Max Based

1.  Open terminal and install git using homebrew 
2.  Enter `brew install git` 
3.  Enter `git clone https://github.com/skydivercactus/simpletrons`  
4.  Enter `cd simpletrons`
5.  Enter `./install.sh`




## Manual Install

For Windows Based

1.  Download Git for Windows ([Download Latest Page](https://gitforwindows.org/)) ([Github v2.33.0 Download Link](https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.2/Git-2.33.0.2-64-bit.exe))
2.  Run the installer to install Git for Windows
3.  Download Python 3.x ([Download Latest Page](https://www.python.org/downloads/windows/)) ([Python 3.9.6 64 bit Download Link](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe))
4.  Ensure “Add Python 3.x to PATH” is checked before “Install Now”
5.  Start Github Bash
6.  Run this command: `pip install opentrons==2.5.2 windows-curses mysql-connector-python`
7.  Enter `git clone https://github.com/skydivercactus/simpletrons`
8.  Enter `cd simpletrons`
9.  Enter `./install.sh`

For Linux (Ubuntu/Debian)
1. `sudo apt-get update && apt-get -y upgrade`
2. `sudo apt-get install -y python3 python3-pip`
3. `git clone https://github.com/skydivercactus/simpletrons`
4. `cd simpletrons`
5. `pip3 install opentrons==2.5.2 windows-curses mysql-connector-python`




If no error occurs, you’re all set. If not, check our FAQ.


# How to run the software

In the Simpletrons directory

In the terminal run `python3 main.py` or `python main.py`

# FAQ

# Installation

## -bash: git: command not found

This is common fix, this error occurred when you don’t have git package installed on your system, please install git.

If you are running unix based (Ubuntu/Debian) Please run `sudo apt update && sudo apt install git` in the terminal window. After that is complete you can retry install step in [readme](https://github.com/skydivercactus/simpletrons/blob/master/README.md).