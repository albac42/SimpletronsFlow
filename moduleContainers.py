##################################################################################
import opentrons
#import openworkstation
from opentrons import robot, containers, instruments
#from openworkstation import robot2
from time import sleep
from moduleCommands import *
##################################################################################

    
def create_container(name, grid_c, grid_r, spacing_c, spacing_r, diameter, depth):
    """ Creating Container """
    print('Creating "', name, '" Container') 
    containers.create(
        name,                    # name of you container
        grid=(grid_c, grid_r),                    # specify amount of (columns, rows)
        spacing=(spacing_c, spacing_r),               # distances (mm) between each (column, row)
        diameter=diameter,                     # diameter (mm) of each well on the plate
        depth=depth                     # depth (mm) of each well on the plate
    )
    #print('Custom Container Created "', name '"')

    #Load Container 
    #var = container.load(name, location, deck)


def load_container(name, location, container):
    """ Load Container """
    print('Loading Container', name) #                       
    name = containers.load(container, location) # Load Container to a location
    print('Loaded Container', name) # 


#Load some useful default containers 
def load_dd_container():
    """ Load Default Container"""
    print ('Loading Default Preset Containers')
    #trashA = containers.load('trash-box', 'A1') 
    #P_A = containers.load('tiprack-1000ul-chem', 'A2')
    #P_B = containers.load('tiprack-1000ul-chem', 'A3')
    print('Loaded default Container')

#create_container(test_c, 10, 10, 2, 5, 5, 1)