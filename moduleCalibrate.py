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


set_calibration_mode = 0


def calibration_mode_toggle(option):
    """ Set Calibration """
    global set_calibration_mode
    
    if option == 1: #Enable
        set_calibration_mode = 1
        print('Enable Calibration Mode')
    if option == 0: #Disable
        set_calibration_mode = 0
        print('Disable Calibration Mode')



def changeDirectionSpeed(speed):
    """ Change Movement Speed Amount"""
    global movementAmount
    if speed > 80:
        print('Warning: Speed Exceed Max Speed Allowed, Please change to lower value <80')
        movementAmount = 80
    if speed < 0.1:
        print('Warning: Speed Exceed Min Speed Allowed, Please change to higher value <0.1')
        movementAmount = 0.1

    movementAmount = speed    
    #print('Speed Set', movementAmount)

position = None

def calibrationControlHome():
    """ Home Robot """
    """ Tested Working """
    global position
    
    if set_calibration_mode == 1:
        robot.home()
        position=list(robot._driver.get_head_position()["current"])
    

def calibrationControl(direction):
    """ Container Calibration Control """
    """ Tested Working """
    global position
    global movementAmount
    global robot

    if ((direction == "z_up") and (set_calibration_mode == 1)):
        position[2]=position[2]+movementAmount

    if ((direction == "z_down") and (set_calibration_mode == 1)):
        position[2]=position[2]-movementAmount

    if ((direction == "x_left") and (set_calibration_mode == 1)):
        position[0]=position[0]-movementAmount

    if ((direction == "x_right") and (set_calibration_mode == 1)):
        position[0]=position[0]+movementAmount

    if ((direction == "y_up") and (set_calibration_mode == 1)):
        position[1]=position[1]+movementAmount

    if ((direction == "y_down") and (set_calibration_mode == 1)):
        position[1]=position[1]-movementAmount
    
    #Send Command To Robot
    robot.move_head(x=position[0],y=position[1],z=position[2])
    position=list(robot._driver.get_head_position()["current"])

def moveDefaultLocation_C(pipette, container, container_type):
    """ Move to Default Location for selected container"""
    """ Tested Working """
    global position
    global pipette_a
    global pipette_b
    
    pos = None
    
    #print(pipette)
    #print(container)

    #Load Pipette
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

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

    if pipette == "pipette_b":
        if container == 'A1':
            A1 = containers.load(container_type, 'A1', 'A1')
            pos = A1[0].from_center(x=0, y=0, z=-1, reference=A1)
            location = (A1, pos)
            pipette_b.move_to(location)
        if container == 'A2':
            A2 = containers.load(container_type, 'A2', 'B2')
            pos = A2[0].from_center(x=0, y=0, z=-1, reference=A2)
            location = (A2, pos)
            pipette_b.move_to(location)
        if container == 'A3':
            A3 = containers.load(container_type, 'A3', 'B3')
            pos = A3[0].from_center(x=0, y=0, z=-1, reference=A3)
            location = (A3, pos)
            pipette_b.move_to(location)
        if container == 'B1':
            B1 = containers.load(container_type, 'B1', 'B1')
            pos = B1[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B1, pos)
            pipette_b.move_to(location)
        if container == 'B2':
            B2 = containers.load(container_type, 'B2', 'B2')
            pos = B2[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B2, pos)
            pipette_b.move_to(location)
        if container == 'B3':
            B3 = containers.load(container_type, 'B3', 'B3')
            pos = B3[0].from_center(x=0, y=0, z=-1, reference=B3)
            location = (B3, pos)
            pipette_b.move_to(location)
        if container == 'C1':
            C1 = containers.load(container_type, 'C1', 'C1')
            pos = C1[0].from_center(x=0, y=0, z=-1, reference=C1)
            location = (C1, pos)
            pipette_b.move_to(location)
        if container == 'C2':
            C2 = containers.load(container_type, 'C2', 'C2')
            pos = C2[0].from_center(x=0, y=0, z=-1, reference=C2)
            location = (C2, pos)
            pipette_b.move_to(location)
        if container == 'C3':
            C3 = containers.load(container_type, 'C3', 'C3')
            pos = C3[0].from_center(x=0, y=0, z=-1, reference=C3)
            location = (C3, pos)
            pipette_b.move_to(location)
        if container == 'D1':
            D1 = containers.load(container_type, 'D1', 'D1')
            pos = D1[0].from_center(x=0, y=0, z=-1, reference=D1)
            location = (D1, pos)
            pipette_b.move_to(location)
        if container == 'D2':
            D2 = containers.load(container_type, 'D2', 'D2')
            pos = D2[0].from_center(x=0, y=0, z=-1, reference=D2)
            location = (D2, pos)
            pipette_b.move_to(location)
        if container == 'D3':
            D3 = containers.load(container_type, 'D3', 'D3')
            pos = D3[0].from_center(x=0, y=0, z=-1, reference=D3)
            location = (D3, pos)
            pipette_b.move_to(location)
        if container == 'E1':
            E1 = containers.load(container_type, 'E1', 'E1')
            pos = E1[0].from_center(x=0, y=0, z=-1, reference=E1)
            location = (E1, pos)
            pipette_b.move_to(location)
        if container == 'E2':
            E2 = containers.load(container_type, 'E2', 'E2')
            pos = E2[0].from_center(x=0, y=0, z=-1, reference=E2)
            location = (E2, pos)
            pipette_b.move_to(location)
        if container == 'E3':
            E3 = containers.load(container_type, 'E3', 'E3')
            pos = E3[0].from_center(x=0, y=0, z=-1, reference=E3)
            location = (E3, pos)
            pipette_b.move_to(location)

    if pipette == "pipette_a":
        if container == 'A1':
            A1 = containers.load(container_type, 'A1', 'A1')
            pos = A1[0].from_center(x=0, y=0, z=-1, reference=A1)
            location = (A1, pos)
            pipette_a.move_to(location)
        if container == 'A2':
            A2 = containers.load(container_type, 'A2', 'A2')
            pos = A2[0].from_center(x=0, y=0, z=-1, reference=A2)
            location = (A2, pos)
            pipette_a.move_to(location)
        if container == 'A3':
            A3 = containers.load(container_type, 'A3', 'A3')
            pos = A3[0].from_center(x=0, y=0, z=-1, reference=A3)
            location = (A3, pos)
            pipette_a.move_to(location)
        if container == 'B1':
            B1 = containers.load(container_type, 'B1', 'B1')
            pos = B1[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B1, pos)
            pipette_a.move_to(location)
        if container == 'B2':
            B2 = containers.load(container_type, 'B2', 'B2')
            pos = B2[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B2, pos)
            pipette_a.move_to(location)
        if container == 'B3':
            B3 = containers.load(container_type, 'B3', 'B3')
            pos = B3[0].from_center(x=0, y=0, z=-1, reference=B3)
            location = (B3, pos)
            pipette_a.move_to(location)
        if container == 'C1':
            C1 = containers.load(container_type, 'C1', 'C1')
            pos = C1[0].from_center(x=0, y=0, z=-1, reference=C1)
            location = (C1, pos)
            pipette_a.move_to(location)
        if container == 'C2':
            C2 = containers.load(container_type, 'C2', 'C2')
            pos = C2[0].from_center(x=0, y=0, z=-1, reference=C2)
            location = (C2, pos)
            pipette_a.move_to(location)
        if container == 'C3':
            C3 = containers.load(container_type, 'C3', 'C3')
            pos = C3[0].from_center(x=0, y=0, z=-1, reference=C3)
            location = (C3, pos)
            pipette_a.move_to(location)
        if container == 'D1':
            D1 = containers.load(container_type, 'D1', 'D1')
            pos = D1[0].from_center(x=0, y=0, z=-1, reference=D1)
            location = (D1, pos)
            pipette_a.move_to(location)
        if container == 'D2':
            D2 = containers.load(container_type, 'D2', 'D2')
            pos = D2[0].from_center(x=0, y=0, z=-1, reference=D2)
            location = (D2, pos)
            pipette_a.move_to(location)
        if container == 'D3':
            D3 = containers.load(container_type, 'D3', 'D3')
            pos = D3[0].from_center(x=0, y=0, z=-1, reference=D3)
            location = (D3, pos)
            pipette_a.move_to(location)
        if container == 'E1':
            E1 = containers.load(container_type, 'E1', 'e1')
            pos = E1[0].from_center(x=0, y=0, z=-1, reference=E1)
            location = (E1, pos)
            pipette_a.move_to(location)
        if container == 'E2':
            E2 = containers.load(container_type, 'E2', 'E2')
            pos = E2[0].from_center(x=0, y=0, z=-1, reference=E2)
            location = (E2, pos)
            pipette_a.move_to(location)
        if container == 'E3':
            E3 = containers.load(container_type, 'E3', 'E3')
            pos = E3[0].from_center(x=0, y=0, z=-1, reference=E3)
            location = (E3, pos)
            pipette_a.move_to(location)

    position=list(robot._driver.get_head_position()["current"])

    print("Successfully Moved to Default Location")


def saveCalibration(rack, pipette, container_type):
    """ Save Container Calibration"""
    global pipette_a
    global pipette_b


    #Load Pipette
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

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

    if pipette == "pipette_b":
        if container == 'A1':
            A1 = containers.load(container_type, 'A1', 'A1')
            pos = A1[0].from_center(x=0, y=0, z=-1, reference=A1)
            location = (A1, pos)
            pipette_b.calibrate_position(location)
        if container == 'A2':
            A2 = containers.load(container_type, 'A2', 'A2')
            pos = A2[0].from_center(x=0, y=0, z=-1, reference=A2)
            location = (A2, pos)
            pipette_b.calibrate_position(location)
        if container == 'A3':
            A3 = containers.load(container_type, 'A3', 'A3')
            pos = A3[0].from_center(x=0, y=0, z=-1, reference=A3)
            location = (A3, pos)
            pipette_b.calibrate_position(location)
        if container == 'B1':
            B1 = containers.load(container_type, 'B1', 'B1')
            pos = B1[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B1, pos)
            pipette_b.calibrate_position(location)
        if container == 'B2':
            B2 = containers.load(container_type, 'B2', 'B2')
            pos = B2[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B2, pos)
            pipette_b.calibrate_position(location)
        if container == 'B3':
            B3 = containers.load(container_type, 'B3', 'B3')
            pos = B3[0].from_center(x=0, y=0, z=-1, reference=B3)
            location = (B3, pos)
            pipette_b.calibrate_position(location)
        if container == 'C1':
            C1 = containers.load(container_type, 'C1', 'C1')
            pos = C1[0].from_center(x=0, y=0, z=-1, reference=C1)
            location = (C1, pos)
            pipette_b.calibrate_position(location)
        if container == 'C2':
            C2 = containers.load(container_type, 'C2', 'C2')
            pos = C2[0].from_center(x=0, y=0, z=-1, reference=C2)
            location = (C2, pos)
            pipette_b.calibrate_position(location)
        if container == 'C3':
            C3 = containers.load(container_type, 'C3', 'C3')
            pos = C3[0].from_center(x=0, y=0, z=-1, reference=C3)
            location = (C3, pos)
            pipette_b.calibrate_position(location)
        if container == 'D1':
            D1 = containers.load(container_type, 'D1', 'D1')
            pos = D1[0].from_center(x=0, y=0, z=-1, reference=D1)
            location = (D1, pos)
            pipette_b.calibrate_position(location)
        if container == 'D2':
            D2 = containers.load(container_type, 'D2', 'D2')
            pos = D2[0].from_center(x=0, y=0, z=-1, reference=D2)
            location = (D2, pos)
            pipette_b.calibrate_position(location)
        if container == 'D3':
            D3 = containers.load(container_type, 'D3', 'D3')
            pos = D3[0].from_center(x=0, y=0, z=-1, reference=D3)
            location = (D3, pos)
            pipette_b.calibrate_position(location)
        if container == 'E1':
            E1 = containers.load(container_type, 'E1', 'E1')
            pos = E1[0].from_center(x=0, y=0, z=-1, reference=E1)
            location = (E1, pos)
            pipette_b.calibrate_position(location)
        if container == 'E2':
            E2 = containers.load(container_type, 'E2', 'E2')
            pos = E2[0].from_center(x=0, y=0, z=-1, reference=E2)
            location = (E2, pos)
            pipette_b.calibrate_position(location)
        if container == 'E3':
            E3 = containers.load(container_type, 'E3', 'E3')
            pos = E3[0].from_center(x=0, y=0, z=-1, reference=E3)
            location = (E3, pos)
            pipette_b.calibrate_position(location)

    if pipette == "pipette_a":
        if container == 'A1':
            A1 = containers.load(container_type, 'A1', 'A1')
            pos = A1[0].from_center(x=0, y=0, z=-1, reference=A1)
            location = (A1, pos)
            pipette_a.calibrate_position(location)
        if container == 'A2':
            A2 = containers.load(container_type, 'A2', 'A2')
            pos = A2[0].from_center(x=0, y=0, z=-1, reference=A2)
            location = (A2, pos)
            pipette_a.calibrate_position(location)
        if container == 'A3':
            A3 = containers.load(container_type, 'A3', 'A3')
            pos = A3[0].from_center(x=0, y=0, z=-1, reference=A3)
            location = (A3, pos)
            pipette_a.calibrate_position(location)
        if container == 'B1':
            B1 = containers.load(container_type, 'B1', 'B1')
            pos = B1[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B1, pos)
            pipette_a.calibrate_position(location)
        if container == 'B2':
            B2 = containers.load(container_type, 'B2', 'A1')
            pos = B2[0].from_center(x=0, y=0, z=-1, reference=B1)
            location = (B2, pos)
            pipette_a.calibrate_position(location)
        if container == 'B3':
            B3 = containers.load(container_type, 'B3', 'B3')
            pos = B3[0].from_center(x=0, y=0, z=-1, reference=B3)
            location = (B3, pos)
            pipette_a.calibrate_position(location)
        if container == 'C1':
            C1 = containers.load(container_type, 'C1', 'C1')
            pos = C1[0].from_center(x=0, y=0, z=-1, reference=C1)
            location = (C1, pos)
            pipette_a.calibrate_position(location)
        if container == 'C2':
            C2 = containers.load(container_type, 'C2', 'C2')
            pos = C2[0].from_center(x=0, y=0, z=-1, reference=C2)
            location = (C2, pos)
            pipette_a.calibrate_position(location)
        if container == 'C3':
            C3 = containers.load(container_type, 'C3', 'C3')
            pos = C3[0].from_center(x=0, y=0, z=-1, reference=C3)
            location = (C3, pos)
            pipette_a.calibrate_position(location)
        if container == 'D1':
            D1 = containers.load(container_type, 'D1', 'D1')
            pos = D1[0].from_center(x=0, y=0, z=-1, reference=D1)
            location = (D1, pos)
            pipette_a.calibrate_position(location)
        if container == 'D2':
            D2 = containers.load(container_type, 'D2', 'D2')
            pos = D2[0].from_center(x=0, y=0, z=-1, reference=D2)
            location = (D2, pos)
            pipette_a.calibrate_position(location)
        if container == 'D3':
            D3 = containers.load(container_type, 'D3', 'D3')
            pos = D3[0].from_center(x=0, y=0, z=-1, reference=D3)
            location = (D3, pos)
            pipette_a.calibrate_position(location)
        if container == 'E1':
            E1 = containers.load(container_type, 'E1', 'E1')
            pos = E1[0].from_center(x=0, y=0, z=-1, reference=E1)
            location = (E1, pos)
            pipette_a.calibrate_position(location)
        if container == 'E2':
            E2 = containers.load(container_type, 'E3', 'E3')
            pos = E2[0].from_center(x=0, y=0, z=-1, reference=E2)
            location = (E2, pos)
            pipette_a.calibrate_position(location)
        if container == 'E3':
            E3 = containers.load(container_type, 'E3', 'E3')
            pos = E3[0].from_center(x=0, y=0, z=-1, reference=E3)
            location = (E3, pos)
            pipette_a.calibrate_position(location)

    calibration_mode_toggle(0)
    print('Calibration Saved')


###########################################################################################################
#
# Pipetting Calibration
#
###########################################################################################################

plungerPos = None

def moveDefaultLocation_p(pipette, plungerTarget):
    """ Moved to Default Pipette Location """
    """ Tested Working """
    global pipette_a
    global pipette_b

    #print(pipette)
    #print(plungerTarget)

    #Load Pipette
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

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


    if pipette == "pipette_b":
        pipette_b.motor.move(pipette_b._get_plunger_position(plungerTarget))
        plungerPos=pipette_b._get_plunger_position(plungerTarget)
        print('Successfully Move To Pipette B Calibration Locations:', pipette)

    if pipette == "pipette_a":
        pipette_a.motor.move(pipette_a._get_plunger_position(plungerTarget))
        plungerPos=pipette_a._get_plunger_position(plungerTarget)
        print('Successfully Move To Pipette A Calibration Locations:', pipette)    

def saveCalibrationPip(pipette, plungerPos):
    """ Save Pip Calibration """
    global pipette_a
    global pipette_b

    #Load Pipette
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

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
    
    
    if pipette == "pipette_b":
        pipette_b.calibrate(plungerPos)
        print('Successfully Save Pipette Calibration:', pipette)

    if pipette == "pipette_a":
        pipette_a.calibrate(plungerPos)
        print('Successfully Save Pipette Calibration:', pipette)

    calibration_mode_toggle(0)

def ControlPlugger(pipette, key, speed):
    """ Save Calibration For Pipette"""
    """ Tested Working """
    global movementAmount
    global plungerPos
    global pipette_a
    global pipette_b
    global set_calibration_mode

    changeDirectionSpeed(speed)
    print(set_calibration_mode)
    #print(pipette)
    
    if ((key == "z_up") and (set_calibration_mode == 1)):
        plungerPos=plungerPos-movementAmount
        print("Calcuate Pos:", plungerPos)

    if ((key == "z_down") and (set_calibration_mode == 1)):
        plungerPos=plungerPos+movementAmount
        print("Calcuate Pos:", plungerPos)

    if ((pipette == "pipette_b") and (set_calibration_mode == 1)):
        pipette_b.motor.move(plungerPos)
        print('Successfully Moved Pipette', pipette)
    if ((pipette == "pipette_a") and (set_calibration_mode == 1)):
        pipette_a.motor.move(plungerPos)
        print('Successfully Moved Pipette', pipette)    

def pip_action_home(pipette):
    """ Move Pipe To Home Position """
    """ Tested Working """

    global plungerPos
    global pipette_a
    global pipette_b
    
    #robot = Robot()
    print(pipette)
    
    print('Homing Pipette')
    """ Pick up Tip"""
    if pipette == "pipette_b":
        pipette_b.home()
        print('Successfully Home Pipette', pipette)
    if pipette == "pipette_a":
        pipette_a.home()
        print('Successfully Home Pipette', pipette)

    plungerPos=0