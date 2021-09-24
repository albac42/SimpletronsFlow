Main Documentation

# Setup Raspberry Pi

Download Raspberry Pi Os Installer ([Raspberry Pi OS – Raspberry Pi)](https://www.raspberrypi.org/software/)

Install Video: [How to use Raspberry Pi Imager | Install Raspberry Pi OS to your Raspberry Pi (Raspbian) - YouTube](https://www.youtube.com/watch?v=ntaXWS8Lk34)

You can now insert the SD card into the Raspberry Pi and power it up. For the official Raspberry Pi OS, if you need to manually log in, the default user name is `pi`, with password `raspberry`. Remember the default keyboard layout is set to UK.

Remember to set a new password if not DO NOT connect to the network. Any data store can be accessible by anyone who has access to the raspberry pi. This is to prevent any unauthorised access to the raspberry pi and associate printers or devices.

Once Raspberry Pi is boot up, please update and install require software. A Internet connection is require to ensure all software is running up to date.

# Configure Simpletrons on Raspberry Pi

1\. Open Terminal

2\. Ensure some preliminary program is installed. `sudo apt install git `

3\. Enter to grab simpletrons latest release `git clone https://github.com/skydivercactus/simpletrons`

4\. Navigate to directory `cd simpletrons`

5\. Run Install Script sudo ./install.sh

6\. Wait until install script finish install

7\. If no error occurred you should be all set to start your first program. (You can ignore any warning occurring in the install script - if you face any error in install script please submit a issues on github https://github.com/skydivercactus/simpletrons/issues/new)

# Configure Simpletrons on Window Based Bash

# Headless Setup

If you wish to setup opentrons headless (without a monitor), please follow below instructions.

1.  After initial raspberry pi setup, please keep SD card plugged into the computer.
2.  Open File Explorer (Windows)/ Finder (Mac) and access portable drive called boot.
3.  create the following files wpa_supplicant.conf and ssh.

File Name: wpa_supplicant.conf

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=AU

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

File name “ssh” without any extension as shown in below Figure.

<img src="https://github.com/skydivercactus/simpletrons/blob/master/docs/images/a16c2a3c9345407ea3bb369447e41763.png" alt="c7c493d8d8e672eef6a16bcef17c3ea0.png" width="687" height="537" class="jop-noMdConv">

4.  Now you can unplug sd card from the computer and insert into raspberry pi.
5.  Plug the power into raspberry pi and give it a few minutes to boot up.
6.  Use a SSH client (PUTTY) to ssh into headless raspberry pi and follow above step to setup simpletrons.

# How to setup correct serial connection to robotic (OT-1)

1.  Please plug in OT-1 communication USB cable into the device.
2.  Please unplug all other USB connection apart from keyboard/mouse.
3.  Check if you simpletrons directory, if not please navigate to that directory using `cd`
4.  Run `python3 tools/toolScanner.py`
5.  Copy/write down serial information.
6.  Open txt named usbserial.txt and paste/enter serial information into it.
7.  Run `python3 calibrate.py` to check if everything is setup correctly, a graphical interface will load if serial has been setup correctly.

# How to use Calibration Application

All OT-1 is require to be calibrate to ensure accuracy of the pipeting robot. This process is REQUIRED to be complete for each new container in the program. You are require to use builtin calibration application to ensure calibration are correctly configured for you custom or pre-defined containers.

Additional Documentations

[OT-One: Calibrating the Deck | Opentrons Help Center](https://support.opentrons.com/en/articles/689977-ot-one-calibrating-the-deck)

[OT-One: Calibrating the Deck | Opentrons Help Center](https://support.opentrons.com/en/articles/689977-ot-one-calibrating-the-deck)

Workspace Reference:

<img src="https://github.com/skydivercactus/simpletrons/blob/master/docs/images/e17a72de9ca94c739ea3faaf78acb5a6.png" alt="DeckMapEmpty.png" width="509" height="454" class="jop-noMdConv">

# How to Calibrate Pipette and Container

1.  Run `python3 main.py`
2.  Select “File - Connections Options”
3.  Select Connect and Home \[Note: You should see the robot home it axis to top right back corner, if not please try manual connection method\] If you still have issues please follow FAQ section regarding USB connectivity.                           ![321ff8a9a4164a852aad40e046727c97.png](https://github.com/skydivercactus/simpletrons/blob/master/docs/images/d93b50c6150d48ccb0880b7308796afa.png)
4.  Select  load all require containers on the workspace, follow the prompts on graphical interfaces. Please enter a value in each box, all measurement are in MM (millimetres). ![6cde9d01d1313d2c169a742df48725d2.png](https://github.com/skydivercactus/simpletrons/blob/master/docs/images/ca5b8a97cbaa4ccc8685adcdde9b4c55.png)
5.  Press Save Workspace
6.  Customised pipetting profile such as max/min volume and desire tip rack and saving. \[Note: If you are using two pipette you need to setup second axis \[Left and Right\] ![d6aeb338d1a822816a622cafa42508f2.png](https://github.com/skydivercactus/simpletrons/blob/master/docs/images/b53ba53889db42f1bb53c4408a39a620.png)
7.  Now confirm the software have connected to robot, press the home button after selecting a pipette and position button.![914658f2e82bc97eccc2ed89ba9809c7.png](https://github.com/skydivercactus/simpletrons/blob/master/docs/images/dca0a90214af4571a00c417a702c2f3b.png)
8.  Use up/down buttons and movement slider to move the piston to desire position.
9.  To confirm position, press the save button and select the next position to calibrate until all 4 position has been calibrate. \[top, button, blow\_out, drop\_tip\]
10. Continue to next step to calibrate each container. 
11. Select pipette and container to calibrate, use the quick access button to go selected container. ![e5c13c2e5fea45cab20b678b4d06b5b5.png](https://github.com/skydivercactus/simpletrons/blob/master/docs/images/fd1fddc741604ef3bc18a07a2f068376.png) 

12 Once all the calibration is calibrated you can go ahead and program protocol