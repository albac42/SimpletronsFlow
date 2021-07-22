from opentrons import robot, containers, instruments
import opentrons
import curses
import time

from curses import wrapper

from moduleCommands import *
from modulePipetting import *
from moduleContainers import *

#Database
import sqlite3
from sqlite3 import Error

#START UP GUI
from tkinter.ttk import Combobox
import tkinter as tk    
from tkinter import ttk


#equipment=getEquipment()

#robot.connect('/dev/ttyACM0')

#robot.connect()

#input("Robot will now home, press enter to continue.")
#robot.home()


#Load Default Containers 

#load_dd_container()

# #Create Blank Array [ Global Variable ]
# placeables = []
# pipettes = [0, 1] #Limit to 2 Pipetting
# count_P = 0
# count_C = 0 


# #Generate Pipettes List
# for axis, pipette in robot.get_instruments():

#     pipettes[count_P]= pipette.name
#     count_P = count_P+1
#     #print(pipette.name)

# #Generate Containers List
# for name, container in robot.get_containers():
#     placeables.append(count_C)
#     placeables[count_C]= name
#     count_C = count_C+1
#     #print(name)

# #Reset Counter
# count_P = 0
# count_C = 0 

# #Global Variables for calibration
# placeableNames=sorted(placeables)
# pipetteNames=sorted(pipettes)

# currentlyCalibrating=placeableNames[0]
# currentPipette=pipetteNames[0]
# movementAmount=1

# #Initial Robotic Position
# position=list(robot._driver.get_head_position()["current"])
# position[0]=0


#print(placeableNames)
#print(pipetteNames)

#position=list(robot._driver.get_head_position()["current"])
#print(position)

def changeDirectionSpeed(speed):
    global movementAmount
    if speed > 80:
        print('Warning: Speed Exceed Max Speed Allowed, Please change to lower value <80')
        movementAmount = 80
    if speed < 0.1:
        print('Warning: Speed Exceed Min Speed Allowed, Please change to higher value <0.1')
        movementAmount = 0.1
    else:    
        movementAmount = speed
        return print('Speed Set', movementAmount)

def calibrationControl(direction):
    global position
    global movementAmount

    if direction == "z_up":
        position[2]=position[2]+movementAmount
        position=list(robot._driver.get_head_position()["current"])
    if direction == "z_down":
        position[2]=position[2]-movementAmount
        position=list(robot._driver.get_head_position()["current"])
    if direction == "x_left":
        position[0]=position[0]-movementAmount
        position=list(robot._driver.get_head_position()["current"])
    if direction == "x_right":
        direction[0]=position[0]+movementAmount
        position=list(robot._driver.get_head_position()["current"])
    if direction == "y_up":
        position[1]=position[1]+movementAmount
        position=list(robot._driver.get_head_position()["current"])
    if direction == "y_down":
        position[1]=position[1]-movementAmount
        position=list(robot._driver.get_head_position()["current"])
    if direction == "home":
        robot.home()
        position=list(robot._driver.get_head_position()["current"])
    else:
        print('Warning: Last action was not sent to robot due to invalid direction command')

        position=list(robot._driver.get_head_position()["current"])

def moveHome():
    robot.home()
    position=list(robot._driver.get_head_position()["current"])

def moveDefaultLocation_C(pipette, container):
    global position
    well = container
    pos = well.from_center(x=0, y=0, z=-1, reference=pipette)
    location = (pipette, pos)
    pipette.move_to(location)
    position=list(robot._driver.get_head_position()["current"])


def moveDefaultLocation_p(pipette, plungerTarget):
    pipette.motor.move(pipette._get_plunger_position(plungerTarget))
    plungerPos=pipette._get_plunger_position(plungerTarget)

def saveCalibration(rack, pipette):
    #pip = pipette
    well = rack[0]
    pos = well.from_center(x=0, y=0, z=-1, reference=rack)
    location = (pipette, pos)
    pipette.calibrate_position(location)
    print('Calibration Saved')

def calibrationControlPlugger(pipette, key):
    global movementAmount
    
    if key == "z_up":
        plungerPos=plungerPos-movementAmount
    elif key == "z_down":
        plungerPos=plungerPos+movementAmount

    pipette.motor.move(plungerPos)

def move_pip_action_home(pipette):
    print(pip)
    pipette.home()
    print('Homing Pipette')
    plungerPos=0

#def selectWhatToCalibrate():






#OLD Curse Calibration Software - NOT FUNCTIONAL - REMOVE CODE WHEN Calibration is fully integrated with UI
#PLEASE USE toolCalibrate.py to use old Calibration CURSE MODE [ Limited to default equipment] - Below Is just a reference 
# movementamounts= {1:0.1, 2:0.5, 3:1, 4:5, 5:10,6:20,7:40,8:80}

# def main(stdscr):
#     currentlyCalibrating=placeableNames[0]
#     currentPipette=pipetteNames[0]
#     movementAmount=1
#     position=list(robot._driver.get_head_position()["current"])
#     position[0]=0
#     def chooseWhatToCalibrate():
#            nonlocal currentlyCalibrating
#            stdscr.clear()
#            stdscr.addstr("What should we calibrate?\n")
#            for i,value in enumerate(placeableNames):
#                stdscr.addstr(str(i+1)+" - " + value+"\n")
#            curses.echo()            # Enable echoing of characters
#            s = stdscr.getstr(20,0, 15)
#            stdscr.addstr(s)
#            currentlyCalibrating=placeableNames[int(s)-1]
#            curses.noecho()
#     def chooseWhatPipetteToCalibrate():
#            nonlocal currentPipette
#            stdscr.clear()
#            stdscr.addstr("What pipette should we calibrate?\n")
#            for i,value in enumerate(pipetteNames):
#                stdscr.addstr(str(i+1)+" - " + value+"\n")
#            curses.echo()            # Enable echoing of characters
#            s = stdscr.getstr(10,0, 15)
#            stdscr.addstr(s)
#            currentPipette=pipetteNames[int(s)-1]
#            curses.noecho()

#     def calibratePlunger():
#            plungerPos=0
#            plungerTarget="top"
#            plungerInc=1
#            while 1:


#                 stdscr.clear()
#                 stdscr.addstr("CALIBRATION - PLUNGER MODE\n\n")
#                 stdscr.addstr("Keyboard shortcuts:\n\n")
#                 stdscr.addstr("T - start calibrating the 'top' position\n")
#                 stdscr.addstr("B - start calibrating the 'bottom' position\n")
#                 stdscr.addstr("O - start calibrating the 'get-new-tip' position\n")
#                 stdscr.addstr("E - start calibrating the 'drop_tip' (eject) position\n\n")
#                 stdscr.addstr("Numbers 1-8 - choose how far to move\n")
#                 stdscr.addstr("Arrow keys - move plunger up/down\n")
#                 stdscr.addstr("S - save this position\n")
#                 stdscr.addstr("M - move to this position\n")
#                 stdscr.addstr("\n\n")
#                 stdscr.addstr("V - switch back to container mode\n\n")
#                 stdscr.addstr("Currently calibrating plunger position: ")
#                 stdscr.addstr( str(plungerTarget)+"\n",curses.A_STANDOUT)
#                 stdscr.addstr("with pipette: ")
#                 stdscr.addstr(str(currentPipette)+"\n",curses.A_STANDOUT)
#                 stdscr.addstr("Movement increment: ")
#                 stdscr.addstr(str(plungerInc)+" mm\n",curses.A_STANDOUT)
#                 stdscr.addstr("Current position -  X: ")
#                 stdscr.addstr(str(plungerPos),curses.A_STANDOUT)

#                 key=stdscr.getkey()
#                 curses.flushinp()
#                 if key=="t":
#                     plungerTarget="top"
#                 if key=="b":
#                     plungerTarget="bottom"
#                 if key=="o":
#                     plungerTarget="blow_out"
#                 if key=="e":
#                     plungerTarget="drop_tip"
#                 if key=="s":
#                     equipment[currentPipette].calibrate(plungerTarget)

#                     stdscr.clear()
#                     stdscr.addstr("plunger position saved")
#                     stdscr.refresh()
#                     time.sleep(1)


#                 if key=="m":
#                     equipment[currentPipette].motor.move(equipment[currentPipette]._get_plunger_position(plungerTarget))
#                     plungerPos=equipment[currentPipette]._get_plunger_position(plungerTarget)
#                 if key=="h":
#                     equipment[currentPipette].home()
#                     plungerPos=0
#                 if key=="v":
#                     return()
#                 try:
#                  if int(key) in movementamounts:
#                     plungerInc=  movementamounts[int(key)]
#                 except ValueError:
#                     pass

#                 if key == "KEY_UP":
#                         plungerPos=plungerPos-plungerInc
#                 if key == "KEY_DOWN":
#                         plungerPos=plungerPos+plungerInc
#                 #stdscr.addstr("Key"+key)

#                 equipment[currentPipette].motor.move(plungerPos)
#                 stdscr.refresh()
    


#     while 1:
#         stdscr.clear()
#         stdscr.addstr("CALIBRATION MODE\n\n")
#         stdscr.addstr("Keyboard shortcuts:\n")
#         stdscr.addstr("P - choose what pipette to calibrate with\n")

#         stdscr.addstr("C - choose what container to calibrate\n")
#         stdscr.addstr("S - save this position\n")
#         stdscr.addstr("H - home\n")
#         stdscr.addstr("M - move to the currently saved position\n\n")
#         stdscr.addstr("Numbers 1-8 - choose how far to move\n")
#         stdscr.addstr("Arrow keys - move forwards/back/left/right\n")
#         stdscr.addstr("Control + arrow keys - move up/down\n\n")
#         stdscr.addstr("V - switch to calibrate this pipette's plunger/volume\n\n")
#         stdscr.addstr("Currently pipette: ")

#         stdscr.addstr(str(currentPipette)+"\n",curses.A_STANDOUT)
#         stdscr.addstr("going to: ")
#         stdscr.addstr(str(currentlyCalibrating)+"\n",curses.A_STANDOUT)

#         stdscr.addstr("Movement increment: ")
#         stdscr.addstr( str(movementAmount)+" mm\n",curses.A_STANDOUT)
#         stdscr.addstr("Current position - ")
#         stdscr.addstr("X:"+ str(position[0])+",Y:"+ str(position[1])+",Z:"+ str(position[2]),curses.A_STANDOUT)

#         key=stdscr.getkey()
#         curses.flushinp()
#         if key=="c":
#             chooseWhatToCalibrate()
#         if key=="v":
#             calibratePlunger()
#         if key=="p":
#             chooseWhatPipetteToCalibrate()
#         if key=="s":

#             well = equipment[currentlyCalibrating][0]
#             pos = well.from_center(x=0, y=0, z=-1, reference=equipment[currentlyCalibrating])
#             location = (equipment[currentlyCalibrating], pos)
#             equipment[currentPipette].calibrate_position(location)
#             stdscr.clear()
#             stdscr.addstr("position saved")
#             stdscr.refresh()
#             time.sleep(1)


#         if key=="m":
#             well = equipment[currentlyCalibrating][0]
#             pos = well.from_center(x=0, y=0, z=-1, reference=equipment[currentlyCalibrating])
#             location = (equipment[currentlyCalibrating], pos)
#             equipment[currentPipette].move_to(location)
#             position=list(robot._driver.get_head_position()["current"])

#         if key=="h":
#             robot.home()
#             position=list(robot._driver.get_head_position()["current"])
#         try:
#          if int(key) in movementamounts:
#             movementAmount=  movementamounts[int(key)]
#         except ValueError:
#             pass

#         if key == "q":
#                 position[2]=position[2]+movementAmount
#         if key == "a":
#                 position[2]=position[2]-movementAmount
#         if key == "KEY_LEFT":
#                 position[0]=position[0]-movementAmount
#         if key == "KEY_RIGHT":
#                 position[0]=position[0]+movementAmount
#         if key == "KEY_UP":
#                 position[1]=position[1]+movementAmount
#         if key == "KEY_DOWN":
#                 position[1]=position[1]-movementAmount
#         if key == "x":
#         	return # Exit Script

#         #stdscr.addstr("Key"+key)

#         robot.move_head(x=position[0],y=position[1],z=position[2])
#         stdscr.refresh()


# #wrapper(main)
