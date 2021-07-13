######################################################################
# Please Do NOT Modify Unless You Know What you're doing #

######################################################################
import opentrons
# Opentrons 2.5.2 (pip install opentrons==2.5.2)
from opentrons import robot, containers, instruments

from modulePipetting import *
from moduleTransportation import getTransportposition
from time import sleep

import sqlite3
from sqlite3 import Error

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
    raise IOError("[#A1]Could not find an Robot - is it plugged in or is serial number setup correct?")

def check_file():
    with open('usbSerial.txt') as f:
        lines = f.readlines() #Read UsbSerial file
        lines = [line.replace(' ', '') for line in lines] #Remove Empty Spaces
    return lines

def find_ot():
    # Run 'python3 tools/toolScanner.py' to obtain serial number for your printer
    serial = check_file()
    print(serial)
    #robotUSB = find_arduino(serial_number='05012004AEFC104858093B9CF50020C3') #Configurable Serial
    robotUSB = find_arduino(serial) #Configurable Serial
    robotUSB = str(robotUSB) #Array to Convert to string
    robotUSB = re.findall(r"port='(.*?)'", robotUSB)
    robotUSB = str(robotUSB) #Array to Convert to string
    robotUSB = str(robotUSB).strip('['']') #Remove Brackets 
    robotUSB = eval(robotUSB) #Remove Quotation

    #print(robotUSB)

#######################################################################

#Connect To both Robot
def connect():
    print('Connecting to Robots')
    # robot.connect()
    find_ot()
    robot.connect(robotUSB)
    print('Opentrons Robot Connected')
    #versions = robot.versions()
    #robot2.connect()
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


##################################################################
# Database
# Test Connection
def create_connection(db_file):
    """ create a test database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print('Datbase Found')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# def clear_database(db_file, table):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)