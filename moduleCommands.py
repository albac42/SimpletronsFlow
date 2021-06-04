######################################################################
# Please Do NOT Modify Unless You Know What you're doing #

######################################################################
import opentrons
# Opentrons 2.5.2 (pip install opentrons==2.5.2)
from opentrons import robot, containers, instruments

from modulePipetting import *
from moduleTransportation import getTransportposition
from time import sleep

import warnings
import serial
import serial.tools.list_ports
import re
######################################################################

# Self Find Serial Port #
def find_arduino(serial_number):
    for pinfo in serial.tools.list_ports.comports():
        if pinfo.serial_number == serial_number:
            return serial.Serial(pinfo.device)
    raise IOError("Could not find an Robot - is it plugged in?")

	robotUSB = find_arduino(serial_number='05012004AEFC104858093B9CF50020C3')
	robotUSB = str(robotUSB)
	robotUSB = re.findall(r"port='(.*?)'", robotUSB)

	#robot2USB = find_arduino(serial_number='16003013AF27A5235A53E460F50020C4')
	#robot2USB = str(robot2USB)
	#robot2USB = re.findall(r"port='(.*?)'", robot2USB)

	print(robotUSB)
	#print(robot2USB)

    #Serial<id=0x75fa4430, open=True>(port='/dev/ttyACM0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
    #Serial<id=0x75fa44f0, open=True>(port='/dev/ttyACM1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)


    #robotUSB = '/dev/ttyACM0'
    #robot2USB = '/dev/ttyACM1'

#######################################################################

#Connect To both Robot
def connect():
    print('Connecting to Robots')
    # robot.connect()
    robot.connect(robotUSB)
    print('Opentrons Robot Connected')
    # robot2.connect()
    #robot2.connect(robot2USB)
    #print('Opentrons Robot Connected')

def home_all():
    print('Homing Opentrons Robot in progress')
    robot.home()
    print('Successfully Homed Opentrons Robot Complete')

    #Home Robot 2
    #robot2._driver.send_command('G28.2 Y Z')
    #robot2._driver.send_command('G28.2 A')
    #robot2._driver.send_command('G28.2 B')
    #robot2._driver.send_command('G28.2 X')
    #robot2._driver.send_command('G90')
    #print('Successfully Homed Transport Robot')

#Homes All Axis For Opentrons Robot
def home_robot():
    print('Homing Opentrons Robot in progress')
    robot.home()
    print('Successfully Homed Opentrons Robot Complete')

#Homes All Axis For Transport Robot
def home_robot2():
    print('Homing Transport Robot in progress')
    robot2._driver.send_command('G28.2 Y Z')
    robot2._driver.send_command('G28.2 A')
    robot2._driver.send_command('G28.2 B')
    robot2._driver.send_command('G28.2 X')
    robot2._driver.send_command('G90')
    print('Successfully Homed Transport Robot')

#Reset Connection
def reset_all():
    #Reset Robot Opentron Robot
    print('Reseting Opentrons Robot')
    robot.reset()
    print('Successfully Rested Opentrons Robot')

    #ResetRobot 2(Transport Platforms)
    #print('Reseting Transport Robot')
    #robot2.reset()
    #print('Successfully Rested Opentrons Robot')
    

def load_calibration():
    print('Loaded Pre-Configured Robot Calibration')