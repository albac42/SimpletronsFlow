###########################################################################################################
#Import Require Library [Do NOT EDIT]
import opentrons

from opentrons import robot, containers, instruments

#from modulePipetting import *
from moduleCommands import *
from moduleContainers import *


#from time import sleep
#import openworkstation
#from openworkstation import
#from moduleCrosslinker import *
#from moduleStorage import *
#from moduleTransportation import getTransportposition

print('Loaded Require Libaries')
print('Loading UI')

try:
    deleteTable("custom_protocol")
    deleteTable("custom_pipette")
    deleteTable("custom_workspace")
except:
	pass
	print("Empty Database - Setup Database")

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

 
###########################################################################################################
"""
Start Module Graphical Front-end
"""
from moduleClass import *
from moduleUI import *
###########################################################################################################

print('UI Closing')
# Delete Temporary Record [Clean Up Database After Closing App]

try:
	deleteTable("custom_protocol")
	deleteTable("custom_pipette")
	deleteTable("custom_workspace")
	print('Application Closed Successfully')
except: 
	print('Error Closing Application - Database did not get flushed correctly')



###########################################################################################################

