import opentrons
#import openworkstation
from opentrons import robot, robot2, containers, instruments
#from opentrons import labware
#from openworkstation import robot2
from time import sleep
from commands import *
from modulePipetting import *
from moduleCrosslinker import *
from moduleStorage import *
from moduleTransportation import getTransportposition

# robot is being reset
#Main Pipetting Robot
robot.reset()
#Robot 2(Transport Platforms)
robot2.reset()

print('connecting to robot')
print('If runtimeerror, please unplug USB and turn off power plug 1. Wait 5s. Replug USB and turn power back on')
#Connection to Robot
connect()
print('connected')
#Home Pipetting and Transport
print('homing all axis')
home_all()
print('homing complete')



#?
#equipment=getEquipment()
#transportposition=getTransportposition()

robot2._driver.send_command('G0 X5 Y5 Z5 A4 B5 F2000')


#Test Containers


#Custom Label Creations
#equipment=getEquipment()

containers.create(
    'custom_test',
    grid=(3 , 6),
    spacing=(12, 12),
    depth = 10,
    diameter=5
    )

custom_plate = containers.load('custom_test', 'A1')


test_pip= instruments.Pipette(
    name='pd1000',
    axis='b',
    max_volume=1000,
    min_volume=100,
    channels=1,
    aspirate_speed=800,
    dispense_speed=1200,
    
    )
    
trash = containers.load('point', 'D2')
tiprack=containers.load('tiprack-200ul', 'A2')

test_pip.pick_up_tip(tiprack.wells('A1'))

for well in custom_plate.wells():
    print(well)


#equipment['pd1000'].move_to(equipment['1000TiprackB2'][1].bottom(-20))


#equipment['pd100'].aspirate(55.0, equipment['MixingD1'].wells('A1').bottom(7.0))
#Move Bottom Rail
#robot2._driver.send_command('G90')
#robot2._driver.send_command(transportposition['modulePipetting'])
#F= Speed (Robot 2 only X axis) transport well plate from storage to pipetting. 
# transportposition is just a saved locations. 
#robot2._driver.send_command('G0 X481 Y5 Z5 A4 B5 F2000')

#Not Working 100% yet
#equipment['pd1000'].move_to(equipment['1000TiprackB2'][4].bottom(-60))
#equipment['pd1000'].delay(seconds=0.5)
#equipment['pd1000'].move_to(equipment['1000TiprackB2'][4.5].bottom(-50))
#pd1000 is left pipet
#equipment['pd1000'].blow_out()

#equipment['pd100'].blow_out()
#equipment['pd100'].move_to(equipment['100TiprackB1'][1].bottom(-100))
#equipment['pd100'].delay(seconds=0.5)
#equipment['pd100'].move_to(equipment['100TiprackB1'][1].bottom(-70))


#equipment['pd1000'].blow_out()
#equipment['pd1000'].move_to(equipment['100TiprackB1'][1].bottom(-98))
#equipment['pd1000'].delay(seconds=0.5)
#equipment['pd1000'].move_to(equipment['100TiprackB1'][1].bottom(-100), strategy='direct')

#tiprack = labware.load('tiprack-200ul' , 'B1')
#pipette = instruments.P300_single(mount='right')
#pipette.pick_up_tip(tiprack.wells('A1'))

#pd100 is right pipet


#move_to_modulePipetting()
#RUN = Inputs
# TIP COUNTERS = [0, 0]
 # 1 = Dilent 2
 # 2 = Dilent 1
# GET TIP (1), i = 4
#pickup_pd1000tip(0)