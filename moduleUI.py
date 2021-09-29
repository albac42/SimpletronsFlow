#Import User Interface Library 
from tkinter import *

#Database
import sqlite3
from sqlite3 import Error

#START UP GUI
from tkinter.ttk import Combobox
import tkinter as tk    
from tkinter import ttk

from opentrons import robot, containers, instruments
import opentrons

#Import RE
import re

#Custom module Imports
from moduleContainers import *
from moduleCommands import *
from moduleCalibrate import *
from modulePipetting import *
#from moduleProtocol import *
###########################################################################################################

# Python TK Graphical Interface Note: [Run on Start]
# Note: This Is Only UI Section (If you want to expand or start from scratch use other python script such as
# moduleProtocol, moduleCommands, moduleCalibrate)

###########################################################################################################

version = 'Version: Private Alpha 1 Dev'

###########################################################################################################
#
# Start Up Command
#
###########################################################################################################
#connect()
create_connection()

###########################################################################################################
#
# Start UI
#
###########################################################################################################
root = Tk()
root.title('Simpletrons - OT')
root.geometry("740x400")
root.pack_propagate(0)

#Setup Windows Location (Center Top Left Corner)
windowWidth = root.winfo_reqwidth() 
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/4 - windowWidth/4)
positionDown = int(root.winfo_screenheight()/4 - windowHeight/4)
root.geometry("+{}+{}".format(positionRight, positionDown))

###########################################################################################################

###########################################################################################################
#
# Global Variable 
#
##########################################################################################################
# Remember to verify the custom container exist before adding into this container list to reduce errors

shortcuts_list = ['Simple_Transfer', 'Multiple_Wells_Transfer', 'One_to_Many', 'Few_to_Many']
container_list = [ '', 'trash-box','point', 'tiprack-10ul', 'tiprack-200ul', 'tiprack-1000ul', '96-flat', 
                    '96-PCR-flat', '96-PCR-tall',  '96-deep-well', '48-well-plate', '24-well-plate',
                   'custom'
                   ]
loaded_pipette_list = ['','']
loaded_container_type = []
loaded_containers = []
count_CT = 0
count_CTT = 0
count_C = 0



###########################################################################################################

###########################################################################################################
#
# Popup Window [If You need create popup windows use below template]
#
###########################################################################################################

def confirmation_box(variable):
    """
    Pop Up Windows Creation
    """
    global version
    global root


    newWindow = Toplevel(root)

    newWindow.title("Simpletrons - OT")
    newWindow.geometry("200x60")

    #Set Window Location
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/3.5 - windowWidth/3.5)
    positionDown = int(root.winfo_screenheight()/3.5 - windowHeight/3.5)
    newWindow.geometry("+{}+{}".format(positionRight, positionDown))

    def close_popup():
        newWindow.destroy()
        newWindow.update()

    def close_popup_protocol_1():
        """Delete Row"""
        count = read_row(custom_protocol)
        deleteRecord(custom_protocol, count)


    if variable == 1:
        newWindow.geometry("200x60")
        label = Label(newWindow, text='Simpletrons - OT', font = ('Arial', 15))
        label.grid(column = 0, row = 0, sticky="NW")
        label2 = Label(newWindow, text=version, font = ('Arial', 15))
        label2.grid(column = 0, row = 1, sticky="NW")

    elif variable == 2:
        newWindow.geometry("180x60")
        label = Label(newWindow, text='Successfully Loaded Workspace', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 3:
        newWindow.geometry("170x60")
        label = Label(newWindow, text='Successfully Loaded Pipette', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 4:
        newWindow.geometry("180x60")
        label = Label(newWindow, text='Successfully Save \n Calibration Pipette', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 5:
        newWindow.geometry("180x60")
        label = Label(newWindow, text='Successfully Save \n Calibration Pipette', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 6:
        newWindow.geometry("170x60")
        label = Label(newWindow, text='Successfully Save \n Pre-Configured Workspace', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 7:
        newWindow.geometry("140x60")
        label = Label(newWindow, text='Successfully Save \n Pre-Configured Pipette', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 7:
        newWindow.geometry("140x60")
        label = Label(newWindow, text='Error Saving Protocol', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup_protocol_1)
        save_w.grid(column = 0, row = 1)

    elif variable == 8:
        newWindow.geometry("140x60")
        label = Label(newWindow, text='Error Saving Pipette \n Check Terminal Window', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 9:
        newWindow.geometry("140x60")
        label = Label(newWindow, text='Error Saving Workspace \n Check Terminal Window', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    elif variable == 10:
        newWindow.geometry("140x60")
        label = Label(newWindow, text='Loaded Custom Pipette', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)

    else:
        newWindow.geometry("180x60")
        label = Label(newWindow, text='Error: Please Check Terminal Window', font = ('Arial', 9))
        label.grid(column = 0, row = 0, sticky="NW")
        save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
        save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
        save_w.grid(column = 0, row = 1)        

###########################################################################################################


###########################################################################################################
#
# Connection To Robot [Pop Up]
#
###########################################################################################################

def connecton_graphical():
    """ Connection UI"""
    """ """
    conroot = Toplevel(root)

    conroot.title("Simpletrons - OT: Protocol - Connection")

    conroot.lift()
    conroot. attributes("-topmost", True)

    def close_popup():
        conroot.destroy()
        conroot.update()
    ###
    s_menu = Menu(root)
    conroot.config(menu = s_menu)

    #Title
    file_menu = Menu(s_menu)
    s_menu.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "Exit", command = close_popup )


    label = ttk.Label(conroot, text = 'Robot Connection Options:')
    label.grid(column = 0, row = 1)

    save_step = ttk.Button(conroot, text = 'Connect', width = 8, command = connect)
    save_step.grid(column = 0, row = 2)

    save_step = ttk.Button(conroot, text = 'Reset', width = 5, command = reset_all)
    save_step.grid(column = 0, row = 3)

    save_step = ttk.Button(conroot, text = 'Manual Connect', width = 16, command = manual_connect)
    save_step.grid(column = 0, row = 4)

    save_step = ttk.Button(conroot, text = 'Home', width = 6, command = home_robot)
    save_step.grid(column = 0, row = 5)

###########################################################################################################

###########################################################################################################
#
# Update Position Pipetting 
#
###########################################################################################################


position_display_xx = StringVar()

position_display_x = StringVar()
position_display_y = StringVar()
position_display_z = StringVar()



def update_position_display():
    """ Update Graphic Position """
    global position_display_x
    global position_display_y
    global position_display_z
    global robot

    position=list(robot._driver.get_head_position()["current"]) 

    position_display_x = ("X:", position[0])
    position_display_y = ("Y:", position[1])
    position_display_z = ("Z:", position[2])

def update_position_display_x():
    """ Update Pipette Position"""
    """ Require more - testing """
    global position_display_xx
    global pipette_a
    global pipette_b
    global plungerPos

    pip = varpip.get()
    plungerTarget = pippos.get()

    #if pip == "pipette_b":
    #    plungerPos = pipette_b._get_plunger_position(plungerTarget)

    #if pip == "pipette_a":
    #     plungerPos = pipette_a._get_plunger_position(plungerTarget)

    #plungerPos = pipette.get_plunger_position(plungerTarget)

    #position_display_xx = ("X:", plungerPos)



###########################################################################################################

###########################################################################################################
#
# Update Container and Pipetting
#
###########################################################################################################


def update_containers_list_type():
    """ Update Type of containers loaded """
    global loaded_container_type
    global count_C

    for name, container in robot.get_containers():
        loaded_container_type.append(count_C)
        loaded_container_type[count_C]= name
        count_C = count_C + 1

    #Sort List
    loaded_container_type = sorted(loaded_container_type)
    print('Loaded Container Type:', loaded_container_type)

def update_containers_list(name):
    """ Update Loaded Container List """
    global loaded_containers
    global count_CT

    loaded_containers.append(count_CT)
    loaded_containers[count_CT]= name
    count_CT = count_CT + 1

#Update Loaded Pipette List
def update_pipette(name, num):
    loaded_pipette_list[num]= name

#Update Tip Rack List in Setup Pipette
def update_dropdown_tip_rack():
    list = loaded_containers
    dropdown_tip_rack['values'] = list
    print('Updating Drop-down List: tip rack pipette setup')

#Update Tip Rack List in Setup Pipette
def update_dropdown_trash():
    list = loaded_containers
    dropdown_trash['values'] = list
    print('Updating Drop-down List: trash pipette setup')

#Update Pipette in Pipette Dropdown
def update_dropdown_pip():
    list = loaded_pipette_list
    dropdown_cpip['values'] = list
    print('Updating Drop-down List: Pipette pipette calibrate')
    calibration_mode_toggle(1)

#Update Pipette in Calibration Dropdown
def update_dropdown_pip_c():
    list = loaded_pipette_list
    dropdown_varpip_c['values'] = list
    print('Updating Drop-down List: Pipette container calibrate')
    calibration_mode_toggle(1)
#Update Container in Calibration Dropdown
def update_dropdown_con_c():
    list = loaded_containers
    dropdown_varcon_c['values'] = list
    print('Updating Drop-down List: containers containers calibrate')
    calibration_mode_toggle(1)

def update_dropdown_pos():
    calibration_mode_toggle(1)


###########################################################################################################

###########################################################################################################
#
# PRE LOAD
#
###########################################################################################################
count_preload_c = 0
count_preload_p = 0

# Load Pre Configured Workspace
def load_pre_workspace(): #For Testing

    global count_preload_c

    if count_preload_c == 0:
        load_container('A1', 'A1', 'trash-box')
        load_container('B1', 'B1', 'tiprack-1000ul')
        load_container('B2', 'B2', 'tiprack-1000ul')
        load_container('C1', 'C1', '24-well-plate')
        load_container('C2', 'C2', '24-well-plate')
        load_container('B3', 'B3', 'point')
        load_container('A3', 'A3', 'point')

        update_containers_list('A1_trash-box')
        update_containers_list('B1_tiprack-1000ul')
        update_containers_list('B2_tiprack-1000ul')
        update_containers_list('C1_24-well-plate')
        update_containers_list('C2_24-well-plate')
        update_containers_list('B3_point')
        update_containers_list('A3_point')


        temp = robot.containers()
        print("Robot Loaded Container List:", temp)

        confirmation_box(6)
        count_preload_c = count_preload_c + 1
    

# Load Pre Configured PIp
def load_pre_pip(): #For Testing
    global count_preload_p

    if count_preload_p == 0:
        #loadpipette ('a', 1000, 100, 800, 1200, 'B1', 'A2')
        insert = ('a', '1000', '100', '1', 800, 1200, 'A1_tiprack-1000ul', 'A2_point')
        save_data("custom_pipette", insert) 
        update_pipette('pipette_a', 1)
        #loadpipette ('b', 1000, 100, 800, 1200, 'B2', 'A2')
        insert = ('b', '1000', '100', '1', 800, 1200, 'A2_tiprack-1000ul', 'A2_point')
        save_data("custom_pipette", insert) 
        update_pipette('pipette_b', 0)
        confirmation_box(7)
        count_preload_p = count_preload_p + 1

###########################################################################################################

###########################################################################################################
#
# Function Link for Calibration
#
###########################################################################################################


#
#Pipette Control
#
def save_pip_action():
    ''' Save Calibration  Pipette'''
    ''' Grab Value from combo box and send to save calibration'''
    pip = varpip.get()
    pos = pippos.get()

    print(pip)
    print(pos)

    saveCalibrationPip(pip, pos)
    confirmation_box(4)

def move_pip_action_up():
    """ Send Pipette Down """
    pip = varpip.get()
    speed = head_speed_p.get()

    ControlPlugger(pip, 'z_up', speed)
    update_position_display_x()

def move_pip_action_down():
    """ Send Pipette Down """
    pip = varpip.get()
    speed = head_speed_p.get()

    ControlPlugger(pip, 'z_down', speed)
    update_position_display_x()

def move_prepip_action():
    """ Send Pipette Pre-Configured Position Command """
    pip = varpip.get()
    plunger = pippos.get()

    moveDefaultLocation_p(pip, plunger)

def move_pip_action_home():
    """ Send Pipette Home Command """
    pip = varpip.get()
    pip_action_home(pip)

##
# Robot Control for calibration
##
def move_x_neg():
    """ Move Robot X Negative"""
    try:
        speed = head_speed_a.get()
        changeDirectionSpeed(speed)
        calibrationControl('x_left')
        update_position_display()
    except:
        print("[K1-XP] Keyboard Input Not Accepted At this Stage") 
    

def move_x_pos():
    """ UI Link to Calibrate Control"""
    try:
        speed = head_speed_a.get()
        changeDirectionSpeed(speed)
        calibrationControl('x_right')
        update_position_display()
    except:
        print("[K1-XP] Keyboard Input Not Accepted At this Stage") 

def move_y_neg():
    try:
        speed = head_speed_a.get()
        changeDirectionSpeed(speed)
        calibrationControl('y_down')
        update_position_display()
    except:
        print("[K1-YN] Keyboard Input Not Accepted At this Stage") 

def move_y_pos():
    try:
        speed = head_speed_a.get()
        changeDirectionSpeed(speed)
        calibrationControl('y_up')
        update_position_display()
    except:
        print("[K1-YP] Keyboard Input Not Accepted At this Stage")  


def move_z_neg():
    try:
        speed = head_speed_a.get()
        changeDirectionSpeed(speed)
        calibrationControl('z_down')
        update_position_display()
    except:
        print("[K1-ZN] Keyboard Input Not Accepted At this Stage") 

def move_z_pos():
    try:
        speed = head_speed_a.get()
        changeDirectionSpeed(speed)
        calibrationControl('z_up')
        update_position_display()
    except:
        print("[K1-ZP] Keyboard Input Not Accepted At this Stage")  

def home_axis():
    calibrationControlHome()

def save_containers_calibration():
    """
    Save Container Calibration
    """
    pip = varpip.get()
    con = c_varcon.get()

    con = con[0:2]

    saveCalibration(con, pip)

    confirmation_box(5)


def load_axis():

    pip = varpip.get()
    con = c_varcon.get()
    
    print("Before:", con)
    contype = con[3:]
    con = con[0:2]
    print(con)

    moveDefaultLocation_C(pip, con, contype)


# Setup Workspace
def setup_workspace():
    """ Setup Workspace Function Link"""

    #Reset Counter
    global count_C
    global count_CT
    global robot

    count_CT = 0

    loaded_containers.clear()
    robot.reset() # Reset Containers

    if A1_W.get() != '':
        print('Entry Found in A1')
        AA = 'A1_'+str(A1_W.get())
        BB = A1_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('A1', 'A1', BB)
        insert = ('A1', BB, 'A1')
        save_data("custom_workspace", insert)

    if A2_W.get() != '':
        print('Entry Found in A2')
        AA = 'A2_'+str(A2_W.get())
        BB = A2_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('A2', 'A2', BB)
        insert = ('A2', BB, 'A2')
        save_data("custom_workspace", insert)

    if A3_W.get() != '':
        print('Entry Found in A3')
        AA = 'A3_'+str(A3_W.get())
        BB = A3_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('A3', 'A3', BB)
        insert = ('A3', BB, 'A3')
        save_data("custom_workspace", insert)

    if B1_W.get() != '':
        print('Entry Found in B1')
        AA = 'B1_'+str(B1_W.get())
        BB = B1_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('B1', 'B1', BB)
        insert = ('B1', BB, 'B1')
        save_data("custom_workspace", insert)

    if B2_W.get() != '':
        print('Entry Found in B2')
        AA = 'B2_'+str(B2_W.get())
        BB = B2_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('B2', 'B2', BB)
        insert = ('B2', BB, 'B2')
        save_data("custom_workspace", insert)

    if B3_W.get() != '':
        print('Entry Found in B3')
        AA = 'B3_'+str(B3_W.get())
        BB = B3_W.get()
        #print(AA)

        update_containecontypers_list(AA)
        load_container('B3', 'B3', BB)
        insert = ('B3', BB, 'B3')
        save_data("custom_workspace", insert)

    if C1_W.get() != '':
        print('Entry Found in C1')
        AA = 'C1_'+str(C1_W.get())
        BB = C1_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('C1', 'C1', BB)
        insert = ('C1', BB, 'C1')
        save_data("custom_workspace", insert)

    if C2_W.get() != '':
        print('Entry Found in C2')
        AA = 'C2_'+str(C2_W.get())
        BB = C2_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('C2', 'C2', BB)
        insert = ('C2', BB, 'C2')
        save_data("custom_workspace", insert)

    if C3_W.get() != '':
        print('Entry Found in C3')
        AA = 'C3_'+str(C3_W.get())
        BB = C3_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('C3', 'C3', BB)
        insert = ('C3', BB, 'C3')
        save_data("custom_workspace", insert)

    if D1_W.get() != '':
        print('Entry Found in D1')
        AA = 'D1_'+str(D1_W.get())
        BB = D1_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('D1', 'D1', BB)
        insert = ('D1', BB, 'D1')
        save_data("custom_workspace", insert)

    if D2_W.get() != '':
        print('Entry Found in D2')
        AA = 'D2_'+str(D2_W.get())
        BB = D2_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('D2', 'D2', BB)
        insert = ('D2', BB, 'D2')
        save_data("custom_workspace", insert)

    if D3_W.get() != '':
        print('Entry Found in D3')
        AA = 'D3_'+str(D3_W.get())
        BB = D3_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('D3', 'D3', BB)
        insert = ('D3', BB, 'D3')
        save_data("custom_workspace", insert)

    if E1_W.get() != '':
        print('Entry Found in E1')
        AA = 'E1_'+str(E1_W.get())
        BB = E1_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('E1', 'E1', BB)
        insert = ('E1', BB, 'E1')
        save_data("custom_workspace", insert)

    if E2_W.get() != '':
        print('Entry Found in E2')
        AA = 'E2_'+str(E2_W.get())
        BB = E2_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('E2', 'E2', BB)
        insert = ('E2', BB, 'E2')
        save_data("custom_workspace", insert)

    if E3_W.get() != '':
        print('Entry Found in E3')
        AA = 'E3_'+str(E3_W.get())
        BB = E3_W.get()
        #print(AA)

        update_containers_list(AA)
        load_container('E3', 'E3', BB)
        insert = ('E3', BB, 'E3')
        save_data("custom_workspace", insert)

    #Update Loaded in Workspace Container List
    try:
        update_containers_list_type()
        print(loaded_containers)
        temp = robot.containers()
        print("Robot Loaded Container List:", temp)

        confirmation_box(2)
    except:
        confirmation_box(9)

def action_save_pip():
    """
    Save Custom Pipette
    Note: The Load Pipette Function is placeholder, it just error checking argument is acceptable
    """
    if var_p_a.get() == 0:
        axis = 'b'
        print(axis)
        update_pipette('pipette_b', 0)
    elif var_p_a.get() == 1:
        axis = 'a'
        print(axis)
        update_pipette('pipette_a', 1)

    max_vol = var_max_volume.get()
    min_vol = var_min_volume.get()
    asp_speed = var_aspirate_speed.get()
    dis_speed = var_dispense_speed.get()


    temp = s_tip_rack.get()
    temp = temp[0:2]

    tiprack = temp
    print(temp)

    temp = s_trash.get()
    temp = temp[0:2]

    trash = temp
    print(temp)

    # print(max_vol)
    # print(min_vol)
    # print(asp_speed)
    # print(dis_speed)

    # print(tiprack)
    # print(trash)

    #Send Command to module load pipette [loadpipette] and save to database [save_data]
    try:
        loadpipette(axis, max_vol, min_vol, asp_speed, dis_speed, tiprack, trash)
        insert = (axis, max_vol, min_vol, '1', asp_speed, dis_speed, tiprack, trash)
        save_data("custom_pipette", insert) 
        print(loaded_pipette_list)

        confirmation_box(10)
    except:
        confirmation_box(8)

###########################################################################################################



###########################################################################################################
#
# Send Job to OT-1 [ WORKING IN PROGRESS ]
#
###########################################################################################################
def opencontainer(location):
    """
    Start Protocol from pre-configured/save protocol from database
    [ WORKING IN PROGRESS ]
    """

    pass


###########################################################################################################

###########################################################################################################
#
# Containers Creation UI [ WORKING IN PROGRESS ]
#
###########################################################################################################
def containersCreationUi():
    """ 
    Graphical UI for Custom Container Creation 
    [ WORKING IN PROGRESS ]

    """

    rootCustomContainer = Tk()
    rootCustomContainer.title('Simpletrons - OT - Container Creation')


    #Create Containers
    var_container_name = StringVar()

    label = ttk.Label(rootCustomContainer, text='Set a Name:', font = ('Arial', 12))
    label.grid(column = 0, row = 1) 
    
    e_container_name = Entry(rootCustomContainer, bd =5, justify = CENTER, textvariable = var_container_name)
    e_container_name.grid(column = 0, row = 2)  


###########################################################################################################
#
# UI Protocol [Pop Up]
#
###########################################################################################################


well_1 = 0
well_2 = 0
dropdown_ppip = StringVar()

#Update Protocol Dropdown
def update_dropdown_source_pip():
    """
    Update source pipette Source Rack Dropdown List for Protocol UI
    """
    list = loaded_pipette_list
    dropdown_ppip['values'] = list
    print('Updating Dropdown List: Pipette Protocol')

def update_aspirate_source_rack():
    """
    Update Aspirate Source Rack Dropdown List for Protocol UI
    """
    list = loaded_containers
    dropdown_aspirate_c['values'] = list
    print('Updating Dropdown List: Containers Protocol')

def update_dispense_source_rack():
    """
    Update Dispense Source Rack Dropdown List for Protocol UI
    """
    list = loaded_containers
    dropdown_dispense_c['values'] = list
    print('Updating Dropdown List: Containers Protocol')

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()

step = 1

def graphicalUIprotocol():
    """ 
    Code for Graphical Protocol Creation 
    Note: Remember to include global variable for any PhotoImage
    """ 

    global v1
    global v2
    global v3 
    global v4
    global shortcuts_list
    global dropdown_dispense_c
    global dropdown_aspirate_c
    global dropdown_ppip
    global dispense_con
    global well_1
    global well_2
    global save_button_image_pro
    global background_image2
    global background_image3
    global background3
    global background2
    global step

    f_name = StringVar()
    volume_well = DoubleVar()
    value_b = StringVar()
    value_c = StringVar()
    f_note = StringVar()
    shortcuts = StringVar()
    p_varpip = StringVar()
    aspirate_con = StringVar()
    dispense_con = StringVar()


    proroot = Toplevel(root)

    proroot.title("Simpletrons - OT: Protocol Designer")
    #newWindow.geometry("200x60")

    def close_popup():
        proroot.destroy()
        proroot.update()

    ###########################################################################################################
    # Start Pre Configured Software 
    ##########################################################################################################
    #Start Protocol
    def start_protocol_ui():

        pass

    ###########################################################################################################
    # Draw Graphics (Containers)
    ########################################################################################################### 

    def callback_a(eventObject):
        ''' Draw Container 1 / a'''
        ''' Use the below template to add more labware photo reference'''
        ''' For instance change re.search to a labware name and PhotoImage'''
        ''' to path of the resource'''

        global background_image2
        global background2
        nonlocal textboxB


        temp = 0

        print(eventObject.widget.get())
        container_lookup = eventObject.widget.get()
        #Grab Value From Entry Box
        if re.search('96-Deep-Well', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/96-Deep-Well.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('96-PCR-flat', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/96-PCR-Flatt.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('96-PCR-tall', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/96-PCR-Tall.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('tiprack-10ul', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/Tiprack-10ul.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('tiprack-1000ul', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/Tiprack-1000.png')
            print("Load Container Image:", container_lookup)            
            temp = 1

        if re.search('96-flat', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/96-PCR-Flatt.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('24-well-plate', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/24-well-plate.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('point', container_lookup):
            background_image2=tk.PhotoImage(file='graphic/labware/point.png')
            print("Load Container Image:", container_lookup)
            temp = 1
            textboxB.grid_forget()

        if bool(re.search('point', container_lookup)) == False:
            #background_image3=tk.PhotoImage(file='graphic/labware/point.png')
            print("Reload Entry Box", container_lookup)
            temp = 1
            textboxB = Entry(proroot, width=12, textvariable=value_c)
            textboxB.grid(column = 1, row = 6)  

        label = ttk.Label(proroot, text="Plate A")
        label.grid(column = 0, row = 9)
        background2 = ttk.Label(proroot, image = background_image2)
        background2.grid(column = 0, row = 10, columnspan = 5)

    #Draw Graphics - Second Container
    def callback_b(eventObject):
        ''' Draw Container 2 / b'''
        ''' Use the below template to add more labware photo reference'''
        ''' For instance change re.search to a labware name and PhotoImage'''
        ''' to path of the resource'''

        global background_image3
        global background3
        nonlocal textboxC

        temp = 0


        print(eventObject.widget.get())
        container_lookup = eventObject.widget.get()
        #Grab Value From Entry Box
        if re.search('96-Deep-Well', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/96-Deep-Well.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('96-PCR-flat', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/96-PCR-Flatt.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('96-PCR-tall', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/96-PCR-Tall.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('tiprack-10ul', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/Tiprack-10ul.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('tiprack-1000ul', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/Tiprack-1000.png')
            print("Load Container Image:", container_lookup)    
            temp = 1        

        if re.search('96-flat', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/96-PCR-Flatt.png')
            print("Load Container Image:", container_lookup)
            temp = 1

        if re.search('24-well-plate', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/24-well-plate.png')
            print("Load Container Image:", container_lookup)
            temp = 1
        if re.search('point', container_lookup):
            background_image3=tk.PhotoImage(file='graphic/labware/point.png')
            print("Load Container Image:", container_lookup)
            temp = 1
            textboxC.grid_forget()

        if bool(re.search('point', container_lookup)) == False:
            #background_image3=tk.PhotoImage(file='graphic/labware/point.png')
            print("Reload Entry Box", container_lookup)
            temp = 1
            textboxC = Entry(proroot, width=12, textvariable=value_b)
            textboxC.grid(column = 3, row = 6)  

        label = ttk.Label(proroot, text="Plate B")
        label.grid(column = 0, row = 11)
        background3 = ttk.Label(proroot, image = background_image3)
        background3.grid(column = 0, row = 12, columnspan = 5)

    ###########################################################################################################
    # Save Steps to Database
    ###########################################################################################################
    def save_step():
        """ Save Step to Database """
        global step
        notes = 'null'
        step_count = False
        # Reference
        # shortcuts_list = ['Simple_Transfer', 'Multiple_Wells_Transfer', 'One_to_Many', 'Few_to_Many']
        print(shortcuts.get())
        if shortcuts.get() == "Simple_Transfer":
            ''' Simple Transfer '''
            #Check if Friendly Name is available if not set a default based of step
            if len(f_name.get()) == 0:
                name = "step" + str(step)
            else:
                name = f_name.get()

            #Shortcut
            shortcuts_v = shortcuts.get()

            #Volume
            volume = volume_well.get()
            #Value 1 (Pipette)
            sel_pipette = p_varpip.get()
            #Value 2 (First Container)
            value1 = aspirate_con.get()
            #Value 2 (First Container Syntax)
            container_lookup = aspirate_con.get()

            #Check if Point Container (Single Well Items)
            if re.search('point', container_lookup):
                value2 = "A1"
            else:
                value2 = value_b.get()
            #Value 3 (Second Container)
            value3 = dispense_con.get()
            #Value 4 (Second Container Syntax)
            container_lookup = dispense_con.get()

            if re.search('point', container_lookup):
                value4 = "A1"
            else:
                value4 = value_b.get()

            if len(f_note.get()) == 0:
                notes = "NULL"
            else:
                notes = f_note.get()


            if tipchange == True:
                option = True
            else:
                option = False

        if shortcuts.get() == "Multiple_Wells_Transfer":
            #Check if Friendly Name is available if not set a default based of step
            if len(f_name.get()) == 0:
                name = "step" + str(step)
            else:
                name = f_name.get()
            #Shortcut
            shortcuts_v = shortcuts.get()

            #Volume
            volume = volume_well.get()
            #Value 1 (Pipette)
            sel_pipette = p_varpip.get()
            #Value 2 (First Container)
            value1 = aspirate_con.get()
            #Value 2 (First Container Syntax)
            container_lookup = aspirate_con.get()

            #Check if Point Container (Single Well Items)
            if re.search('point', container_lookup):
                value2 = "A1"
            else:
                step_count = True
                confirmation_box(7)



            value3 = dispense_con.get()

            # Code To Find if row or column ()
            # If you need higher rows count adjust pattern2
            pattern1 = re.compile("[A-Za-z]+")
            pattern2 = re.compile("[0-12]+")
            container_lookup = dispense_con.get()

            if pattern1.fullmatch(container_lookup) is not None:
                value4 = dispense_con.get()
                option2 = "cols"
            if pattern2.fullmatch(container_lookup) is not None:
                value4 = dispense_con.get()
                option2 = "rows"
            else:
                step_count = True
                confirmation_box(7)

            if len(f_note.get()) == 0:
                notes = "NULL"
            else:
                notes = f_note.get()

            if tipchange == True:
                option = True
            else:
                option = False

        if shortcuts.get() == "One_to_Many":
            pass

        if shortcuts.get() == "Few_to_Many":
            pass

        insert = (name, shortcuts_v, sel_pipette, volume, value1, value2, value3, value4, option, option2, notes)
        save_data("custom_protocol", insert)

        step = step + 1

        #Reset Count if error occurs in step creation 
        if step_count == True:
            step = step - 1
            step_count = False


    ###########################################################################################################

    ###########################################################################################################
    # Menu
    ###########################################################################################################

    ###
    s_menu = Menu(root)
    proroot.config(menu = s_menu)

    #Title
    file_menu = Menu(s_menu)
    start_protocol_menu = Menu(s_menu)
    s_menu.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "Exit", command = close_popup )
    start_protocol_menu.add_command(label = "Start Protocol", command = start_protocol_ui)
    ####

    ###########################################################################################################
    # Draw Main Graphical Interface
    ###########################################################################################################

    # Short Cut Function
    label = ttk.Label(proroot, textvariable=v1)
    label.grid(column = 0, row = 0)
    v1.set("Transfer: Basic") #Set Default Label

    label = ttk.Label(proroot, text = 'Shortcuts Function:*')
    label.grid(column = 0, row = 1)
    
    dropdown_shortcuts = ttk.Combobox(proroot, textvariable = shortcuts)
    dropdown_shortcuts['values'] = shortcuts_list
    dropdown_shortcuts.current(0)   #Set Default Selection
    dropdown_shortcuts.grid(column = 0, row = 2)

    # Friendly Note Input
    label = ttk.Label(proroot, text="Friendly Note:")
    label.grid(column = 2, row = 1)
    textboxF = Entry(proroot, textvariable=f_note)
    textboxF.grid(column = 2, row = 2)

    tipchange = None

    #Change Tip Tick Box
    label = ttk.Label(proroot, text="Change Tip?")
    label.grid(column = 2, row = 3)
    textboxI = Checkbutton(proroot, variable=tipchange, text='Never')
    textboxI.grid(column = 2, row = 4)    
    textboxI.select()

    # Friendly Name Input
    label = ttk.Label(proroot, text="Friendly Name:")
    label.grid(column = 1, row = 1)
    textboxF = Entry(proroot, width=12, textvariable=f_name)
    textboxF.grid(column = 1, row = 2)

    #Select Pipette
    label = ttk.Label(proroot, text = 'Pipette:*')
    label.grid(column = 0, row = 3)
    dropdown_ppip = ttk.Combobox(proroot, textvariable = p_varpip, postcommand = update_dropdown_source_pip)
    dropdown_ppip.grid(column = 0, row = 4)

    label = ttk.Label(proroot, textvariable=v2)
    label.grid(column = 1, row = 3)
    v2.set("Volume Per Well: (uL)*") #Set Default Label
    textboxA = Entry(proroot, width=12, textvariable=volume_well)
    textboxA.grid(column = 1, row = 4)

    #First Container
    label = ttk.Label(proroot, text = 'Aspirate:*')
    label.grid(column = 0, row = 5)
    dropdown_aspirate_c = ttk.Combobox(proroot, textvariable = aspirate_con, postcommand = update_aspirate_source_rack)
    dropdown_aspirate_c.grid(column = 0, row = 6)
    dropdown_aspirate_c.bind("<<ComboboxSelected>>", callback_a)

    label = ttk.Label(proroot, textvariable=v3)
    label.grid(column = 1, row = 5)
    v3.set("Wells:*") #Set Default Label
    textboxB = Entry(proroot, width=12, textvariable=value_b)
    textboxB.grid(column = 1, row = 6)

    #Second Container
    label = ttk.Label(proroot, text = 'Dispense:*')
    label.grid(column = 2, row = 5)
    dropdown_dispense_c = ttk.Combobox(proroot, textvariable = dispense_con, postcommand = update_dispense_source_rack)
    dropdown_dispense_c.grid(column = 2, row = 6)
    dropdown_dispense_c.bind("<<ComboboxSelected>>", callback_b)

    label = ttk.Label(proroot, textvariable=v4)
    label.grid(column = 3, row = 5)
    v4.set("Wells:*") #Set Default Label
    textboxC = Entry(proroot, width=12, textvariable=value_c)
    textboxC.grid(column = 3, row = 6)

    #Save Button
    save_button_image_pro = PhotoImage(file="graphic/content-save-outline.png") 
    save_step = ttk.Button(proroot, image = save_button_image, width = 5, command = save_step)
    save_step.grid(column = 4, row = 6)





##########################################################################################################

###########################################################################################################
#
#
#
# Calibration UI
#
#
#
###########################################################################################################
# root = Tk()
# root.title('Simpletrons - OT')
###########################################################################################################
#
#Tab Creation
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab1b = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

#Tab Header Name
tabControl.add(tab1b, text ='Step 1 Containers Setup')
tabControl.add(tab1, text ='Step 2 Pipette Setup')
tabControl.add(tab2, text ='Step 3 Calibrate Pipette')
tabControl.add(tab3, text ='Step 4 Calibrate Containers')
#tabControl.add(tab4, text ='Step 3 Protocol Programmer')
#tabControl.add(tab5, text ='Step 4 Start Protocol')

tabControl.pack(expand = 1, fill ="both")
#tabControl.grid(column = 3, row = 1, padx = 1)

########################################################################################################
#
#Top Menu 
#
#########################################################################################################

def aboutPage():
    confirmation_box(1)
    pass

s_menu = Menu(root)
root.config(menu = s_menu)

file_menu = Menu(s_menu)
s_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New Protocol..." , command=graphicalUIprotocol)
file_menu.add_command(label = "Connections Options", command = connecton_graphical)
file_menu.add_command(label = "About", command = aboutPage)
file_menu.add_command(label = "Exit", command = root.quit )


#Start Up UI
#connecton_graphical()
########################################################################################################
#
#Container Setup
#
A1_W = StringVar(root, value='')
A2_W = StringVar(root, value='')
A3_W = StringVar(root, value='')
B1_W = StringVar(root, value='')
B2_W = StringVar(root, value='')
B3_W = StringVar(root, value='')
C1_W = StringVar(root, value='')
C2_W = StringVar(root, value='')
C3_W = StringVar(root, value='')
D1_W = StringVar(root, value='')
D2_W = StringVar(root, value='')
D3_W = StringVar(root, value='')
E1_W = StringVar(root, value='')
E2_W = StringVar(root, value='')
E3_W = StringVar(root, value='')

background_image=PhotoImage(file='graphic/workspace.png')
my_canvas = ttk.Label(tab1b, image = background_image)
my_canvas.grid(column = 0, row = 0, rowspan = 3, columnspan = 5)

#Col A
dropdown = ttk.Combobox(tab1b, textvariable = A1_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 0, row = 2, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = A2_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 0, row = 1, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = A3_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 0, row = 0, padx = 1)
dropdown.lift()

#Col B
dropdown = ttk.Combobox(tab1b, textvariable = B1_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 1, row = 2, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = B2_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 1, row = 1, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = B3_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 1, row = 0, padx = 1)
dropdown.lift()

#Col C
dropdown = ttk.Combobox(tab1b, textvariable = C1_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 2, row = 2, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = C2_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 2, row = 1, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = C3_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 2, row = 0, padx = 1)
dropdown.lift()

#Col D
dropdown = ttk.Combobox(tab1b, textvariable = D1_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 3, row = 2, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = D2_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 3, row = 1, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = D3_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 3, row = 0, padx = 1)
dropdown.lift()
#Col E
dropdown = ttk.Combobox(tab1b, textvariable = E1_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 4, row = 2, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = E2_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 4, row = 1, padx = 1)
dropdown.lift()

dropdown = ttk.Combobox(tab1b, textvariable = E3_W, width = 19)
dropdown['values'] = container_list 
dropdown.grid(column = 4, row = 0, padx = 1)
dropdown.lift()

#Save Button - Save Workspace 
label = ttk.Label(tab1b, text='Save Workspace:', font = ('Arial', 12))
label.grid(column = 1, row = 3)

save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
save_w = ttk.Button(tab1b, image = save_button_image, width = 5, command = setup_workspace)
save_w.grid(column = 2, row = 3)

#Save Button - Load Pre-Configured Workspace
label = ttk.Label(tab1b, text='Load Workspace:', font = ('Arial', 12))
label.grid(column = 3, row = 3)

pree_home_image = PhotoImage(file="graphic/cog-refresh-outline.png")
save_w = ttk.Button(tab1b, image = pree_home_image, width = 5, command = load_pre_workspace)
save_w.grid(column = 4, row = 3)

#Button

########################################################################################################




########################################################################################################
#
#Calibrate Containers
#
########################################################################################################
#Drop Down Default Selection
varpip = StringVar(root, value='')
head_speed_a = DoubleVar()

#Selection 1 - Pipette
label = ttk.Label(tab3, text='Select a Pipette', font = ('Arial', 12))
label.grid(column = 1, row = 1, padx = 1)
dropdown_varpip_c = ttk.Combobox(tab3,  state="readonly" , textvariable = varpip, postcommand = update_dropdown_pip_c)
dropdown_varpip_c.grid(column = 1, row = 2, padx = 1)

#Drop Down Default Selection
c_varcon = StringVar(root, value='')

#Selection 1 - Containers
label = ttk.Label(tab3, text='Select a Container', font = ('Arial', 12))
label.grid(column = 1, row = 3, padx = 1)
dropdown_varcon_c = ttk.Combobox(tab3,  state="readonly", textvariable = c_varcon, postcommand = update_dropdown_con_c)
dropdown_varcon_c.grid(column = 1, row = 4, padx = 1)

#Section 2 - Pipette Movement 

#Pipette Movement Increments
#Movement Pad - X Axis
#Set Image to variable
xn_button_image = PhotoImage(file="graphic/arrow-left-bold-circle.png") # [ X Axis Negative ]
left_b = ttk.Button(tab3, image = xn_button_image, width = 5, command = move_x_neg)
left_b.grid(column = 3, row = 2)

#Movement Pad - X Axis
#Set Image to variable 
xp_button_image = PhotoImage(file="graphic/arrow-right-bold-circle.png") # [ X Axis Positive ]
right_b = ttk.Button(tab3, image = xp_button_image, width = 5, command = move_x_pos)
right_b.grid(column = 5, row = 2)

#Movement Pad - Y Axis
#Set Image to variable
yn_button_image = PhotoImage(file="graphic/arrow-up-bold-circle.png")  # [ y Axis Postive ]
down_b = ttk.Button(tab3, image = yn_button_image, width = 5, command = move_y_pos)
down_b.grid(column = 4, row = 1)

#Movement Pad - Y Axis
#Set Image to variable
yp_button_image = PhotoImage(file="graphic/arrow-down-bold-circle.png") # [ y Axis Negative ]
up_b = ttk.Button(tab3, image = yp_button_image, width = 5, command = move_y_neg)
up_b.grid(column = 4, row = 3)


#Movement Pad - Z Axis [Pipette Movement] Down
zd_button_image = PhotoImage(file="graphic/arrow-down-bold-circle.png")  # [ Z Axis Negative ]
z_up_b = ttk.Button(tab3, image = zd_button_image, width = 5, command = move_z_neg)
z_up_b.grid(column = 3, row = 3)

#Movement Pad - Z Axis [Pipette Movement] UP
zu_button_image = PhotoImage(file="graphic/arrow-up-bold-circle.png") # [ z Axis Positive ]
z_down_b = ttk.Button(tab3, image = zu_button_image, width = 5, command = move_z_pos)
z_down_b.grid(column = 3, row = 1)

#Home
home_image = PhotoImage(file="graphic/home.png") 
home_b = ttk.Button(tab3, image = home_image, width = 5, command = home_axis)
home_b.grid(column = 4, row = 4)

#Move to preconfigured 
pre_home_image = PhotoImage(file="graphic/cog-refresh-outline.png")
pre_home_b = ttk.Button(tab3, image = pre_home_image, width = 5, command = load_axis)
pre_home_b.grid(column = 5, row = 4)

#Save Button - Calibration 
#save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
save_c = ttk.Button(tab3, image = save_button_image, width = 5, command = save_containers_calibration)
save_c.grid(column = 3, row = 4)


#Change Movement Speed
label = ttk.Label(tab3, text='Set Movement Speed:', font = ('Arial', 10))
label.grid(column = 1, row = 5)
#Scale Bar
scale_a = Scale(tab3, from_=0.1, to=80, resolution = 0.1, orient="horizontal", variable = head_speed_a)
scale_a.grid(column = 1, row = 6)
#Sync Entry Box
text = Entry(tab3, width=4, textvariable=head_speed_a)
text.grid(column = 0, row = 6, padx=5)
text.bind("<Return>", lambda event: scale_a.configure(to=head_speed_a.get()))
#Unit
label = ttk.Label(tab3, text='mm', font = ('Arial', 10))
label.grid(column = 2, row = 6)


label = ttk.Label(tab3, text='Robot Position:', font = ('Arial', 10))
label.grid(column = 1, row = 7)
#Display Coordinate
label = ttk.Label(tab3, textvariable=position_display_xx)
label.grid(column = 0, row = 8)
position_display_xx.set("x: 0") #Set Default Label

label = ttk.Label(tab3, textvariable=position_display_y)
label.grid(column = 1, row = 8)
position_display_y.set("y: 0") #Set Default Label

label = ttk.Label(tab3, textvariable=position_display_z)
label.grid(column = 2, row = 8)
position_display_z.set("z: 0") #Set Default Label

#Keyboard Input
# root.bind("<Left>", move_x_neg)
# root.bind("<Right>", move_x_pos)
# root.bind("<Up>", move_y_neg) 
# root.bind("<Down>", move_y_pos)

def key_press(event):
    if event.char == "R":
        move_z_neg()
    if event.char == "r":
        move_z_neg()
    if event.char == "f":
        move_z_pos()
    if event.char == "F":
        move_z_pos()
    if event.char == "a":
        move_x_neg()
    if event.char == "d":
        move_x_pos()
    if event.char == "w":
        move_y_neg()
    if event.char == "s":
        move_y_pos()

    pass

root.bind("<Key>", key_press)

#########################################################################################################
#
#Setup Pipette
#
#########################################################################################################
#Drop Down Default Selection
#varcon = StringVar(root, value='')
var_p_a = IntVar()
var_max_volume = DoubleVar()
var_min_volume = DoubleVar()
var_aspirate_speed = DoubleVar()
var_dispense_speed = DoubleVar()
s_tip_rack = StringVar(root, value='')
s_trash = StringVar(root, value='')



#Selection 1 - Axis
label = ttk.Label(tab1, text='Select a Axis:', font = ('Arial', 12))
label.grid(column = 1, row = 0)
#Scale Bar
scale_1 = Scale(tab1, from_=0, to=1, resolution = 1, orient="horizontal", variable = var_p_a)
scale_1.grid(column = 1, row = 1)

left_hand_image = PhotoImage(file="graphic/hand-left.png")
right_hand_image = PhotoImage(file="graphic/hand-right.png")

label = ttk.Label(tab1, image=left_hand_image).grid(column = 0,  row =0)
label = ttk.Label(tab1, text='L', font = ('Arial', 12) ).grid(column = 0,  row =1)
label = ttk.Label(tab1, image=right_hand_image).grid(column = 2,  row =0)
label = ttk.Label(tab1, text='R', font = ('Arial', 12) ).grid(column = 2,  row =1)

#Selection 2 - Max Volume
var_max_volume = IntVar()

label = ttk.Label(tab1, text='Select a max volume:', font = ('Arial', 12))
label.grid(column = 1, row = 2)
#Scale Bar
scale_2 = Scale(tab1, from_=0, to=500, resolution = 1, orient="horizontal", variable = var_max_volume)
scale_2.grid(column = 1, row = 3)
#Sync Entry Box
text = Entry(tab1, width=3, textvariable=var_max_volume)
text.grid(column = 0, row = 3, padx=5)
text.bind("<Return>", lambda event: scale_2.configure(to=var_max_volume.get()))
#Unit
label = ttk.Label(tab1, text='uL', font = ('Arial', 12))
label.grid(column = 2, row = 3)

#Selection 3 - Min Volume
var_min_volume = IntVar()

label = ttk.Label(tab1, text='Select a min volume:', font = ('Arial', 12))
label.grid(column = 1, row = 4)
#Scale Bar
scale_3 = Scale(tab1, from_=0, to=500, resolution = 1, orient="horizontal", variable = var_min_volume)
scale_3.grid(column = 1, row = 5)
#Sync Entry Box
text = Entry(tab1, width=3, textvariable=var_min_volume)
text.grid(column = 0, row = 5, padx=5)
text.bind("<Return>", lambda event: scale_3.configure(to=var_min_volume.get()))
#Unit
label = ttk.Label(tab1, text='uL', font = ('Arial', 12))
label.grid(column = 2, row = 5)

#Selection 3 - aspirate_speed
var_aspirate_speed = IntVar()

label = ttk.Label(tab1, text='Select aspirate speed:', font = ('Arial', 12))
label.grid(column = 1, row = 6)
#Scale Bar
scale_4 = Scale(tab1, from_=100, to=600, resolution = 1, orient="horizontal", variable = var_aspirate_speed)
scale_4.grid(column = 1, row = 7)
#Sync Entry Box
text = Entry(tab1, width=3, textvariable=var_aspirate_speed)
text.grid(column = 0, row = 7, padx=5)
text.bind("<Return>", lambda event: scale_4.configure(to=var_aspirate_speed.get()))
#Unit
label = ttk.Label(tab1, text='mm/min', font = ('Arial', 12))
label.grid(column = 2, row = 7)

# Separator object
separator = ttk.Separator(tab1, orient='vertical')
separator.grid(row=0,column=4, rowspan=10, ipady=180)

#Selection 4 - dispense_speed
var_dispense_speed = IntVar()

label = ttk.Label(tab1, text='Select a dispense speed:', font = ('Arial', 12))
label.grid(column = 1, row = 8)
#Scale Bar
scale_5 = Scale(tab1, from_=100, to=600, resolution = 1, orient="horizontal", variable = var_dispense_speed)
scale_5.grid(column = 1, row = 9)
#Sync Entry Box
text = Entry(tab1, width=3, textvariable=var_dispense_speed)
text.grid(column = 0, row = 9, padx=5)
text.bind("<Return>", lambda event: scale_5.configure(to=var_dispense_speed.get()))
#Unit
label = ttk.Label(tab1, text='mm/min', font = ('Arial', 12))
label.grid(column = 2, row = 9)

#Selection 5 - Select a Tip Rack
label = ttk.Label(tab1, text='Select a Tip Rack:', font = ('Arial', 12))
label.grid(column = 6, row = 0)
dropdown_tip_rack = ttk.Combobox(tab1, state="readonly",  textvariable = s_tip_rack, postcommand = update_dropdown_tip_rack)
#dropdown['values'] = loaded_containers # Replace to Global pipette variable
dropdown_tip_rack.grid(column = 6, row = 1)

#Selection 6 - Select a Bin
label = ttk.Label(tab1, text='Select a Bin:', font = ('Arial', 12))
label.grid(column = 6, row = 2)
dropdown_trash = ttk.Combobox(tab1,  state="readonly" , textvariable = s_trash, postcommand = update_dropdown_trash)
#dropdown['values'] = loaded_containers # Replace to Global pipette variable
dropdown_trash.grid(column = 6, row = 3)

# Save Button
label = ttk.Label(tab1, text='Save Pipette Config:', font = ('Arial', 12))
label.grid(column = 6, row = 4)
save_pip = ttk.Button(tab1, image = save_button_image, width = 5, command = action_save_pip)
save_pip.grid(column = 6, row = 5)

# Separator object
separator = ttk.Separator(tab1, orient='vertical')
separator.grid(row=0,column=8, rowspan=10, ipady=180)

#Use Pre-Configured Pipetting in script/database
label = ttk.Label(tab1, text='Load Pre-Configured:', font = ('Arial', 12))
label.grid(column = 6, row = 6)
pre_select_pip = ttk.Button(tab1, image = pre_home_image, width = 5, command = load_pre_pip)
pre_select_pip.grid(column = 6, row = 7)


#########################################################################################################
#
#Calibrate Pipette
#
#########################################################################################################
#Change Photo
#Load Graphics According to Position Calibration
vpc1 = StringVar()
head_speed_p = DoubleVar()

def callback_p(eventObject):
    global vpc1

    global background_img_pc
    global background_image_pc

    if eventObject.widget.get() == "top":
        background_image_pc=tk.PhotoImage(file='graphic/calibrate/Top.png')
        vpc1.set("Top: Plunger is positioned almost all the way up (but still being \n pressed down just a tiny bit")

    if eventObject.widget.get() == "bottom":
        background_image_pc=tk.PhotoImage(file='graphic/calibrate/Bottom.png')
        vpc1.set("Bottom: Plunger is at or slightly above it’s “first-stop” or “soft-stop” ")

    if eventObject.widget.get() == "blow_out":
        background_image_pc=tk.PhotoImage(file='graphic/calibrate/Blowout.png')
        vpc1.set("Blow Out: Plunger is all the way down to it's “second-stop” or \n “hard-stop”,  making sure any attached tip do not get pushed off")

    if eventObject.widget.get() == "drop_tip":
        background_image_pc=tk.PhotoImage(file='graphic/calibrate/Blowout.png')
        vpc1.set("Drop Tip: Forces any attached tip to fall off ")

    background_img_pc = ttk.Label(tab2, image = background_image_pc)
    background_img_pc.grid(column = 6, row = 2, rowspan = 7)

    label = ttk.Label(tab2, textvariable=vpc1)
    label.grid(column = 6, row = 1)


#Selection 1 - Pipette
label = ttk.Label(tab2, text='Select a Pipette:', font = ('Arial', 12))
label.grid(column = 1, row = 1, padx = 1)
dropdown_cpip = ttk.Combobox(tab2,  state="readonly", textvariable = varpip, postcommand = update_dropdown_pip)
dropdown_cpip.grid(column = 1, row = 2, padx = 1)

#Drop Down Default Selection
pippos = StringVar(root, value=' ')
#Selection 2 - Which Selection
label = ttk.Label(tab2, text='Select a Position:', font = ('Arial', 12))
label.grid(column = 1, row = 3, padx = 1)
dropdown_cpos = ttk.Combobox(tab2,  state="readonly", textvariable = pippos, postcommand = update_dropdown_pos)
dropdown_cpos['values'] = [ 'top','bottom', 'blow_out','drop_tip']
dropdown_cpos.grid(column = 1, row = 4, padx = 1)
dropdown_cpos.bind("<<ComboboxSelected>>", callback_p)

#Pipette Movement Increments
#Movement Pad - Z Axis [Pipette Movement] Down
z_up_bp = ttk.Button(tab2, image = zd_button_image, width = 5, command = move_pip_action_down)
z_up_bp.grid(column = 3, row = 3)

#Movement Pad - Z Axis [Pipette Movement] UP 
z_down_bp = ttk.Button(tab2, image = zu_button_image, width = 5, command = move_pip_action_up)
z_down_bp.grid(column = 3, row = 1)

#Home Button
home_b = ttk.Button(tab2, image = home_image, width = 5, command = move_pip_action_home)
home_b.grid(column = 4, row = 4)

#Move to pre configured 
pre_home_b = ttk.Button(tab2, image = pre_home_image, width = 5, command = move_prepip_action)
pre_home_b.grid(column = 5, row = 4)

#Save Button - Calibration  
save_p = ttk.Button(tab2, image = save_button_image, width = 5, command = save_pip_action)
save_p.grid(column = 3, row = 4)

#Change Movement Speed
label = ttk.Label(tab2, text='Set Movement Speed:', font = ('Arial', 10))
label.grid(column = 1, row = 5)
#Scale Bar
scale_b = Scale(tab2, from_=0.1, to=10, resolution = 0.1, orient="horizontal", variable = head_speed_p)
scale_b.grid(column = 1, row = 6)
#Sync Entry Box
text = Entry(tab2, width=4, textvariable=head_speed_p)
text.grid(column = 0, row = 6, padx=5)
text.bind("<Return>", lambda event: scale_b.configure(to=head_speed_p.get()))
#Unit
label = ttk.Label(tab2, text='mm', font = ('Arial', 10))
label.grid(column = 2, row = 6)

label = ttk.Label(tab2, text='Robot Position:', font = ('Arial', 10))
label.grid(column = 1, row = 7)
#Display Coordinate
label = ttk.Label(tab2, textvariable=position_display_x)
label.grid(column = 1, row = 8)
position_display_x.set("x: 0") #Set Default Label


#Keyboard Input
# root.bind("<Prior>", move_pip_action_up) #Page UP
# root.bind("<Next>", move_pip_action_down) #PageDown


def key_press(event):
    if event.char == "R":
        move_pip_action_up()
    if event.char == "r":
        move_pip_action_up()
    if event.char == "f":
        move_pip_action_down()
    if event.char == "F":
        move_pip_action_down()

root.bind("<Key>", key_press)



#########################################################################################################

root.mainloop() 
#########################################################################################################

#Debugging (Run Graphical Interface without backend code)