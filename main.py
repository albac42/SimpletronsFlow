###########################################################################################################
#Import Require Library [Do NOT EDIT]
import opentrons

from opentrons import robot, containers, instruments

#from modulePipetting import *
from moduleCommands import *
from moduleContainers import *
from moduleClass import *

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

###########################################################################################################
""" 
Custom Container

Example:
create_container( [name of you container], [specify amount of columns], [specify amount of rows], 
					 [distances (mm) between each column], [distances (mm) between each row], 
					 [diameter (mm) of each well on the plate], [depth (mm) of each well on the plate])

"""
create_container('custom', 3, 3, 10, 10, 15, 5)
###########################################################################################################
# Test Data [Use this to test Protocol API without front-end]
def test_save_data():
    """ Debugging Temp Data"""

    #1 Setup Pipette Default
    # Axis , max volume , min volume, channel (1 or 8), aspirate speed, dispense speed, tip rack, bin
    insert = ('b', '1000', '100', '1', 800, 1200, 'A2_tiprack-1000ul', 'B2_point')
    save_data("custom_pipette", insert) 

    #2 Setup Bare Minimal Workspace
    name = "A1" # Container Name
    container = "24-well-plate" # Container Type 
    location = "A1" # Location Position on workspace
    x = "44.068" #Manual Calibration Data [DO NOT EDIT If you don't know actual value]
    y = "14.4053"
    z = "-65.9"
    xx = "0"
    yy ="0"
    zz = "0"

    insert = (name, container, location, x, y, z, xx, yy, zz)
    save_data("custom_workspace", insert)

    name = "B1" # Container Name
    container = "48-well-plate" # Container Type 
    location = "B1" # Location Position on workspace
    x = "131.0789" #Manual Calibration Data [DO NOT EDIT If you don't know actual value]
    y = "15.46" # Pipette B
    z = "-67.8"
    xx = "0"
    yy ="0"
    zz = "0"

    insert = (name, container, location, x, y, z, xx, yy, zz)
    save_data("custom_workspace", insert)
    
    name = "B2" # Container Name
    container = "B2_point" # Container Type 
    location = "B2" # Location Position on workspace
    x = "159.0074" #Manual Calibration Data [DO NOT EDIT If you don't know actual value]
    y = "190.4798"
    z = "-46.0"
    xx = "0"
    yy ="0"
    zz = "0"

    insert = (name, container, location, x, y, z, xx, yy, zz)
    save_data("custom_workspace", insert)
    
    name = "A2" # Container Name
    container = "A2_tiprack-1000ul" # Container Type 
    location = "A2" # Location Position on workspace
    x = "39.2424" #Manual Calibration Data [DO NOT EDIT If you don't know actual value]
    y = "146.85"
    z = "-72"
    xx = "0"
    yy ="0"
    zz = "0"

    insert = (name, container, location, x, y, z, xx, yy, zz)
    save_data("custom_workspace", insert)

    #4 Step Demo (Simple Transfer)
    name = "Step 1" # Step Name 
    shortcuts = "Simple_Transfer" #Transfer Shortcut [Refer To Documentation]
    sel_pipette = "pipette_b" # Pipette Name (pipette_b or pipette_a)
    volume = 100 # Volume (Double Variable)
    value1 = "B1_48-well-plate"  #First Plate Full Name (Require initial 3 variable is require for location)
    value2 = "B1" #Well Cell for first plate
    value3 = "B1_48-well-plate" #Second Plate Full Name (Require initial 3 variable is require for location)
    value4 = "B2" #Well Cell for second plate
    option = True #Never Change Tip Enable (False for always change tip)
    option2 = None #Additional Parameters 
    notes = "Simple Transfer From 24 well plate to 48 well plate"

    #Insert To Database Function
    insert = (name, shortcuts, sel_pipette, volume, value1, value2, value3, value4, option, option2, notes)
    save_data("custom_protocol", insert)
    
    
    #5 Step Demo (one to many)
    name = "Step 2" 
    shortcuts = "One_to_Many"
    sel_pipette = "pipette_b"
    volume = 200
    value1 = "A1_24-well-plate"
    value2 = "A2"
    value3 = "B1_48-well-plate"
    value4 = "1"
    option = True
    option2 = 'rows' # For one to Many you can set to transfer to whole rows or cols by changing this. 
                    # DO not value need to just a number (rows) or a letter (cols)
    notes = "test notes"

    #Insert To Database Function
    insert = (name, shortcuts, sel_pipette, volume, value1, value2, value3, value4, option, option2, notes)
    save_data("custom_protocol", insert)   
###########################################################################################################
"""
Start Module Graphical Front-end
"""

from moduleUI import *
###########################################################################################################

print('UI Closing')
# Delete Temporary Record [Clean Up Database After Closing App]

try:
	deleteTable("custom_protocol")
	deleteTable("custom_pipette")
	deleteTable("custom_workspace")
	print('Application Closed Succesfully')
except: 
	print('Error Closing Application - Database did not get flushed correctly')



###########################################################################################################

