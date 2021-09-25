######################################################################
#Import Require Library [Do NOT EDIT]
import opentrons

from opentrons import robot, containers, instruments

#from modulePipetting import *
from moduleCommands import *
#from moduleContainers import *

#from time import sleep
#import openworkstation
#from openworkstation import
#from moduleCrosslinker import *
#from moduleStorage import *
#from moduleTransportation import getTransportposition

print('Loaded Require Libaries')
print('Loading UI')

setup_table("custom_protocol")
setup_table("custom_pipette")
setup_table("custom_workspace")

from moduleUI import *
print('UI Closing')


# Manual Python Method [Old Code - Ignore]
######################################################################

#Startup Scripts [Do NOT EDIT]

#Reset main Pipetting Robot & Transport Robot 
#reset_all()

#Connection to Robot
#connect()
#home_all() # Home all system


#home_robot() # Home Just Opentrons Robot
#home_robot2() #Home Storage Robot 

#Load Calibration 
#load_calibration()

######################################################################

#Create Custom Containers [Editable]
#Note: Please Create and load All Custom Containers Here
#Note: Name Should not contain any spaces

#create_container(name, grid_c, grid_r, spacing_c, spacing_r, diameter, 
#	depth, deck)

#Refer to Desk Documentation

#Example Container
#create_container('test_c', 10, 10, 2, 5, 5, 1)



#######################################################################

#Loading Pre-built containers onto workspace [Editable]
#Load Additional containers onto the Deck that wasn't just created
#load_container(name, location, var):

#Load Default Containers (Refer to Documentation)
#load_dd_container()

#Load Containers
#load_container('test_c', 'A1')

#######################################################################

# Create and configure Pipette [Editable]

# Please check documentation or user manual for correct Pipetting Device 
#loadpipette (a, 200, 100, 1000TiprackB2, TrashA2)


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





# Delete Temporary Record 
deleteTable("custom_protocol")
deleteTable("custom_pipette")
deleteTable("custom_workspace")




