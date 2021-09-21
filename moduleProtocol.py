from opentrons import robot, containers, instruments
#from opentrons import robot2

from moduleCommands import *
from moduleContainers import *
from modulePipetting import *
from time import sleep

# This Module require modules such as modulePipetting and moduleContainer
# and moduleCommand to function. SQL function are majority built in function
# below but some are reference using moduleCommands
# Please edit below test_save_data if you play around wish to use
# code to write your protocol. Please refer to documentation for more info 

def start_protocol():
    """Start Protocol based on information in database"""
    """ Any database shortcut please refer to moduleCommands"""
    """ Basic Transfer Supported """
    """ Other Shortcuts is currently WIP """
    step_count = read_row('custom_protocol')
    print(step_count)

    #Connection to Custom Protocol Table
    conn = sqlite3.connect(db_file)
    c = conn.cursor()


    #Load Pipette
    sqlite_select_query = """SELECT * FROM custom_pipette"""
    c.execute(sqlite_select_query) 
    for row in c:
        print(row)


    #Load Containers in loaded in workspace
    sqlite_select_query = """SELECT * FROM custom_workspace"""
    c.execute(sqlite_select_query) 
    for row in c:
        print(row)


    #Load protocol in loaded in workspace
    sqlite_select_query = """SELECT * FROM custom_protocol"""
    c.execute(sqlite_select_query) 
    # Basic Tranfer
    for row in c:
        print(row)

        volume = row[4]

        plateA = row[5]
        wellA = row[6]

        plateB = row[7]
        wellB = row[8]

        pipette = row[3]
        #Send Action to Robot
        if pipette == "pipette_b":

            plateA = plateA[0:2]
            plateB = plateB[0:2]

            #pipette_b.transfer(volume, plateA.wells(wellA), plateB.wells(wellB))


        if pipette == "pipette_a":
            #pipette_a.transfer(volume, plateA.wells(wellA), plateB.wells(wellB))
            pass


    #Exit Database 
    conn.close() 


def test_save_data():
    """ Debugging Temp Data"""

    #1 Setup Pipette Default


    #2 Setup Bare Minimal Workspace
    name = "C1"
    container = "24-well-plate"
    location = "C1"

    insert = (name, container, location)
    save_data("custom_workspace", insert)

    name = "C2"
    container = "24-well-plate"
    location = "C2"

    insert = (name, container, location)
    save_data("custom_workspace", insert)

    #2 Step Demo (Simple Transfer)
    name = "Step 1"
    shortcuts = "Simple_Transfer"
    sel_pipette = "pipette_a"
    volume = 20
    value1 = "C1_24-well-plate"
    value2 = "C2"
    value3 = "C2_24-well-plate"
    value4 = "A2"
    notes = "test notes"

    insert = (name, shortcuts, sel_pipette, volume, value1, value2, value3, value4, notes)
    save_data("custom_protocol", insert)

    name = "Step 2"
    shortcuts = "Simple_Transfer"
    sel_pipette = "pipette_a"
    volume = 20
    value1 = "C1_24-well-plate"
    value2 = "D2"
    value3 = "C2_24-well-plate"
    value4 = "D2"
    notes = "test notes"

    insert = (name, shortcuts, sel_pipette, volume, value1, value2, value3, value4, notes)
    save_data("custom_protocol", insert)    


#Load Test Data Condition [Comment Out if you require debugging Protocol API]
#It will load a test data

# Start 
setup_table("custom_protocol")
setup_table("custom_pipette")
setup_table("custom_workspace")
test_save_data() #Load Test data in database
start_protocol() #Start Protocol
deleteTable("custom_protocol")
deleteTable("custom_pipette")
deleteTable("custom_workspace")

# Old Cross Linking Platform Code
# If you wish to work on this section, you require custom library from original raspberry pi with
# library "robot2" , standalone library does not include robot2 from opentrons pip library.
#

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
