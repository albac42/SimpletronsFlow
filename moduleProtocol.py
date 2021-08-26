from opentrons import robot, containers, instruments
#from opentrons import robot2

from moduleCommands import *
from time import sleep


















# Old Cross Linking Paltform
#transportposition = getTransportposition()

# intensity range
# PWM = (0-(-0.1251))/0.0161 = 8.0

# example: intensity = 2.5
# PWM = (2.5-(-0.1251))/0.0161 = 163

#lightON = 'M106'
#lightOFF = 'M107'

# def crosslinking():
#     # absolute movement
#     robot._driver.send_command('G90')
#     # move plate in crosslinker module
#     move_to_moduleCrosslinker()
#     # specifiy intensity
#     robot2._driver.send_command('G0 Z280')
#     # define PWM value for specified intensity
#     # example
#     robot2._driver.send_command('M106 S132')
#     # LEDs on
#     robot2._driver.send_command(lightON)
#     # crosslinking duration in seconds
#     # sleep(duration)
#     # example
#     # duration = 120 s
#     sleep(30)
#     # LEDs off
#     robot2._driver.send_command(lightOFF)
