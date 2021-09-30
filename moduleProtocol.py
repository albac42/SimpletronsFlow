from opentrons import robot, containers, instruments
#from opentrons import robot2

from moduleCommands import *
from moduleContainers import *
from modulePipetting import *
from time import sleep


# For Jupiter Environment  
# from opentrons.util import environment
# environment.refresh()
# print(environment.get_path('CALIBRATIONS_FILE'))

# import os
# del os.environ['calibrations/calibrations.json']
# environment.refresh()

"""
 This Module require modules  modulePipetting and moduleContainer
 and moduleCommand to function. SQL read function are majority built in function
 below but some are reference using moduleCommands
 Please edit below test_save_data if you play around wish to use
 code to write your protocol. Please refer to documentation for more info 
"""

def start_protocol():
    """
    Start Protocol based on information in database
    Any database shortcut please refer to moduleCommands
    Basic Transfer Supported 
    Other Shortcuts is currently WIP [Additional columns may be required for database more options]
    This API will grab all steps and send command to OT-1
    """
    #Home Robot (Note: Require user to be connected to robot using connection UI (Manual or Auto))
    manual_connect()    
    home_robot()


    step_count = read_row('custom_protocol')
    print(step_count)

    #Connection to Custom Protocol Table
    conn = sqlite3.connect(db_file)
    c = conn.cursor()


    #Load Pipette
    # Load Blank Default Pipette
    pipette_a = instruments.Pipette(
        axis='b',
        max_volume=200)
    pipette_b = instruments.Pipette(
        axis='a',
        max_volume=200)

    sqlite_select_query = """SELECT * FROM custom_pipette"""
    c.execute(sqlite_select_query) 
    for row in c:
        print(row)

        rawTip = row[7]
        rawTrash = row[8]

        tipName = rawTip[0:2]
        tipType = rawTip[3:]

        trashName = rawTrash[0:2]
        trashType = rawTrash[3:]

        tiprack = containers.load(trashType, tipName)
        trash =containers.load(tipType, trashName)

        axis_s = row[1]

        if axis_s == 'b':
            pipette_b = instruments.Pipette(
            axis='b',
            name='pipette_b',
            max_volume=row[2],
            min_volume=row[3],
            channels = row[4],
            aspirate_speed=row[5],
            dispense_speed=row[6],
            tip_racks=tiprack,
            trash_container=trash
            )
            print ("Loaded B Axis Pipette")

        if axis_s == 'a':
            pipette_a = instruments.Pipette(
            axis='a',
            name='pipette_a',
            max_volume=row[2],
            min_volume=row[3],
            channels = row[4],
            aspirate_speed=row[5],
            dispense_speed=row[6],
            tip_racks=tiprack,
            trash_container=trash
            )
            print ("Loaded A Axis Pipette")




    #Load protocol in loaded in workspace
    sqlite_select_query = """SELECT * FROM custom_protocol"""
    c.execute(sqlite_select_query) 
    """ Basic Transfer
    Load Temp Custom Protocol 
    It will read each row and send command for each step.
    Uncomment out print(row) if you wish to see output.

    """
    for row in c:
        print(row)

        #Load Variable from database row
        id_count = row[0]

        shortcut = row[2]

        volume = row[4]

        plateA = row[5]
        wellA = row[6]

        plateB = row[7]
        wellB = row[8]

        pipette = row[3]

        option = row[9]

        option2 = row[10]

        #Note: https://docs.opentrons.com/ot1/transfer.html 
        #Use above resource for opentrons API shortcut
        #Send Action to Robot 
        if shortcut == "Simple_Transfer":
            ''' [ Simple Transfer ] '''
            if pipette == "pipette_b":

                #First Plate Initialisation 
                plateAName = plateA[0:2]
                planteAType = plateA[3:]
                print(plateAName)
                #print(planteAType)

                plateA = containers.load(planteAType, plateAName)
                
                #Load Calibration Data
                calibarate_data = find_data("custom_workspace", plateAName)
                #pipette_b.move_to(calibarate_data)
                robot.move_head(x=calibarate_data[0],y=calibarate_data[1],z=60)
                robot.move_head(z=calibarate_data[2])

                pos = plateA[0].from_center(x=0, y=0, z=-1, reference=plateA)
                pipette_b.calibrate_position((plateA, pos))


                #Second Plate Initialisation 
                plateBName = plateB[0:2]
                planteBType = plateB[3:]
                #print(plateBName)
                #print(planteBType)

                plateB = containers.load(planteBType, plateBName)

                print(option)
                # Check Tip Check Condition
                if option == '1':
                    pipette_b.transfer(volume, plateA.wells(wellA), plateB.wells(wellB), new_tip='never')
                    print("Complete: Step", id_count, ": Option: Never Change")

                else:
                    pipette_b.transfer(volume, plateA.wells(wellA), plateB.wells(wellB), new_tip='always')
                    print("Complete: Step", id_count, ": Option: Always")

            if pipette == "pipette_a":

                plateAName = plateA[0:2]
                planteAType = plateA[3:]
                #print(plateAName)
                #print(planteAType)

                plateA = containers.load(planteAType, plateAName)

                plateBName = plateB[0:2]
                planteBType = plateB[3:]
                #print(plateBName)
                #print(planteBType)

                plateB = containers.load(planteBType, plateBName)

                if option == '1':
                    pipette_a.transfer(volume, plateA.wells(wellA), plateB.wells(wellB), new_tip='never')
                    print("Complete: Step", id_count, ": Option: Never Change")

                else:
                    pipette_a.transfer(volume, plateA.wells(wellA), plateB.wells(wellB), new_tip='always')
                    print("Complete: Step", id_count, ": Option: Always")

        if shortcut == "One_to_Many":
            ''' One_to_Many
            [ You can transfer from a single source to multiple destinations, and the other way around 
            (many sources to one destination).  ] 
            '''
            if pipette == "pipette_b":

                plateAName = plateA[0:2]
                planteAType = plateA[3:]
                #print(plateAName)
                #print(planteAType)

                plateA = containers.load(planteAType, plateAName)

                plateBName = plateB[0:2]
                planteBType = plateB[3:]
                #print(plateBName)
                #print(planteBType)

                plateB = containers.load(planteBType, plateBName)


                if option2 == "rows":
                    # Never Get a New Tip each steps
                    if option == '1':
                        pipette_b.transfer(volume, plateA.wells(wellA), plateB.rows(wellB), new_tip='never')

                    if option == '0':
                        pipette_b.transfer(volume, plateA.wells(wellA), plateB.rows(wellB), new_tip='always')

                if option2 == "cols":
                    if option == '1':
                        pipette_b.transfer(volume, plateA.wells(wellA), plateB.cols(wellB), new_tip='never')

                    if option == '0':
                        pipette_b.transfer(volume, plateA.wells(wellA), plateB.cols(wellB), new_tip='always')                    

            if pipette == "pipette_a":

                plateAName = plateA[0:2]
                planteAType = plateA[3:]
                #print(plateAName)
                #print(planteAType)

                plateA = containers.load(planteAType, plateAName)

                plateBName = plateB[0:2]
                planteBType = plateB[3:]
                #print(plateBName)
                #print(planteBType)

                plateB = containers.load(planteBType, plateBName)

                if option2 == "rows":
                    # Never Get a New Tip each steps
                    if option == '1':
                        pipette_a.transfer(volume, plateA.wells(wellA), plateB.rows(wellB), new_tip='never')

                    if option == '0':
                        pipette_a.transfer(volume, plateA.wells(wellA), plateB.rows(wellB), new_tip='always')

                if option2 == "cols":
                    if option == '1':
                        pipette_a.transfer(volume, plateA.wells(wellA), plateB.cols(wellB), new_tip='never')

                    if option == '0':
                        pipette_a.transfer(volume, plateA.wells(wellA), plateB.cols(wellB), new_tip='always') 




    #Exit Database 
    conn.close() 

# Test Data [Use this to test Protocol API without front-end]
def test_save_data():
    """ Debugging Temp Data"""

    #1 Setup Pipette Default
    # Axis , max volume , min volume, channel (1 or 8), aspirate speed, dispense speed, tip rack, bin
    insert = ('b', '1000', '100', '1', 800, 1200, 'A1_tiprack-1000ul', 'A2_point')
    save_data("custom_pipette", insert) 

    #2 Setup Bare Minimal Workspace
    name = "A1" # Container Name
    container = "24-well-plate" # Container Type 
    location = "A1" # Location Position on workspace
    calibration = "(13.67, 15.00, 0.00)" #Manual Calibration Data [DO NOT EDIT If you don't know actual value]

    insert = (name, container, location, calibration)
    save_data("custom_workspace", insert)

    name = "B1" # Container Name
    container = "48-well-plate" # Container Type 
    location = "B1" # Location Position on workspace
    calibration = "(10.08, 18.16, 0.00)" #Manual Calibration Data [DO NOT EDIT If you don't know actual value]

    insert = (name, container, location, calibration)
    save_data("custom_workspace", insert)

    #3 Step Demo


    #4 Step Demo (Simple Transfer)
    name = "Step 1" # Step Name 
    shortcuts = "Simple_Transfer" #Transfer Shortcut [Refer To Documentation]
    sel_pipette = "pipette_b" # Pipette Name (pipette_b or pipette_a)
    volume = 30 # Volume (Double Variable)
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
    sel_pipette = "pipette_a"
    volume = 30
    value1 = "A1_24-well-plate"
    value2 = "A2"
    value3 = "B1_48-well-plate"
    value4 = "2"
    option = True
    option2 = 'rows' # For one to Many you can set to transfer to whole rows or cols by changing this. 
                    # DO not value need to just a number (rows) or a letter (cols)
    notes = "test notes"

    #Insert To Database Function
    insert = (name, shortcuts, sel_pipette, volume, value1, value2, value3, value4, option, option2, notes)
    save_data("custom_protocol", insert)    


#Load Test Data Condition [Comment Out if you require debugging Protocol API]
#It will load a test data

# Start 
setup_table("custom_protocol")
setup_table("custom_pipette")
setup_table("custom_workspace")


test_save_data() #Load Test data in database
start_protocol() #Start Protocol

"""
You would need to delete table upon exiting database 

If you getting data base lock, you need to delete database/data.db and 
recreate the file. 

You can start cleardatabase.py to reset the database to default
[This is only require if the code crash during protocol]

"""
deleteTable("custom_protocol") 
deleteTable("custom_pipette")
deleteTable("custom_workspace")

# Cross Linking Platform Code
# If you wish to work on this section, you require custom library from original raspberry pi with
# library "robot2" , standalone library does not include robot2 from opentrons pip library.
# 
# Another method is to copy original robot api from original source 

#transportposition = getTransportposition()

# intensity range
# PWM = (0-(-0.1251))/0.0161 = 8.0

# example: intensity = 2.5
# PWM = (2.5-(-0.1251))/0.0161 = 163

# lightON = 'M106'
# lightOFF = 'M107'

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
