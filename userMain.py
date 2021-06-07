######################################################################
#Import Require Library [Do NOT EDIT]
import opentrons
#import openworkstation
from opentrons import robot, containers, instruments
#from openworkstation import
from time import sleep
#from commands import *
from modulePipetting import *
from moduleCrosslinker import *
from moduleStorage import *
from moduleTransportation import getTransportposition
from moduleCommands import *
from moduleContainers import *
print('Loaded Require Libaries')

######################################################################

#Startup Scripts [Do NOT EDIT]

#Reset main Pipetting Robot & Transport Robot
reset_all()

#Connection to Robot
connect()
home_all() # Home all system

#home_robot() # Home Just Opentrons Robot
#home_robot2() #Home Storage Robot 

#Load Calibration 
load_calibration()

######################################################################

#Create Custom Containers [Editable]
#Note: Please Create and load All Custom Containers Here
#Note: Name Should not contain any spaces

#create_container(name, grid_c, grid_r, spacing_c, spacing_r, diameter, 
#	depth, deck)

#Refer to Desk Documentation

#Example Container
create_container(test_c, 10, 10, 2, 5, 5, 1)



#######################################################################

#Loading Pre-built containers onto workspace [Editable]
#Load Additional containers onto the Deck that wasn't just created
#load_container(name, location, var):

#Load Default Containers (Refer to Documentation)
load_dd_container()

#######################################################################

# Create and configure Pipette [Editable]

# Please check documentation or user manual for correct Pipetting Device 


loadpipette_b()
#######################################################################

# Pick Up Tip Function Editable

# Pick up Tip 

# pickuptip (a, 'A1') # Using Pipetting A to pick tip from A1 
#



# Function Aspirate
# aspirate(plate, amount, well) 
# Example
#f_aspirate(custom_plate, 10, 'A1') # Aspirate 10uL from custom_plate:A1 cell


# Function Dispense
# dispense(plate, amount, well) 
# Example
#f_dispense(custom_96, 5, 'A1') # Aspirate 10uL from custom_96:A1 cell


#Function Blow Out [ Remove Excess Liquid]
# f_blowout() # Blowout Liquid at current location
# f_blowout(bin) # Blowout Liquid at loaded contain named bin
# f_blowout(custom_96, 'A1') # Blowout liquid at selected well on  plate


#Function Touch Tip
#Move Pipette tip to the edge of selected well wall 
#f_touchtip() # Touch tip at current location


#Function Mix 
#Mix Current Solution
#f_mix(2, 20)  # mix 2 times, 20uL, in current location


#Function Air Gap
#Aspirate Air into Tip [Require to be added after Aspirate]
#f_air(20) # Aspirate 20ul airgap

#Change Tip Command


#Pre-Built Function
#Delay between each serials if command [On in progress]
#Option to enable Touch Tip for every/selected dispense option
#Option to enable mixing on every/selected dispense option
#Option to enable Air Gap for every/selected dispense option










######################################################################################################
#Testing Code [Ignore - Will be remove for production]


#?
#equipment=getEquipment()
#transportposition=getTransportposition()

#robot2._driver.send_command('G0 X5 Y5 Z5 A4 B5 F2000')



#Custom Label Creations
#Container 

#containers.create(
#    '3x6_plate',                    # name of you container
#    grid=(3, 6),                    # specify amount of (columns, rows)
#    spacing=(12, 12),               # distances (mm) between each (column, row)
#    diameter=5,                     # diameter (mm) of each well on the plate
#    depth=10                        # depth (mm) of each well on the plate
#    )                       


#trashA = container.load('point', 'A1')      #Load a Blank container  (Trash/Scale)
#trashB = container.load('point', 'B1')      #Load a Blank container  (Trash/Scale)


#custom_plate = containers.load('3x6_plate', 'D1')


#pipette_left = instruments.Pipette(
#    axis='b',
#    name='my-p200',
#    max_volume=200,
#    min_volume=20
#    )



#pipette_right = instruments.Pipette(
#    axis='a',
#    name='my-p200',
#    max_volume=200,
#    min_volume=20
#    )




#pipette.pick_up_tip(tiprack.wells('A1'))


#strategy='direct'



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