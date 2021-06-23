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
from moduleContainers import *
from moduleCommands import *

#Global Variable
container_list = [ '', 'trash','96_tip', '96_well' ]

load_dd_container()
#connect()
create_connection('database/data.db')

def list_containers():

	return 

def graphicalUIprotocol(): # Start Graphical Protocal Interface
	pass

def aboutPage():
	pass

###########################################################################################################
#
# Containers Creation UI
#
###########################################################################################################
def containersCreationUi():
	rootNew = Tk()
	rootNew.title('Simpletrons - OT - Container Creation')


	#Create Containers
	var_container_name = StringVar()

	label = ttk.Label(rootNew, text='Set a Name:', font = ('Arial', 12))
	label.grid(column = 0, row = 1)	
	
	e_container_name = Entry(rootNew, bd =5, justify = CENTER, textvariable = var_container_name)
	e_container_name.grid(column = 0, row = 2)	



###########################################################################################################
#
# Calibration UI
#
###########################################################################################################
def graphicalUIcalibrate():
	root = Tk()
	root.title('Simpletrons - OT')
	########################################################################################################
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
	#Top Menu 
	s_menu = Menu(root)
	root.config(menu = s_menu)

	file_menu = Menu(s_menu)
	s_menu.add_cascade(label = "File", menu = file_menu)
	file_menu.add_command(label = "New Protocol..." , command=graphicalUIprotocol)
	file_menu.add_command(label = "About", command = aboutPage)
	file_menu.add_command(label = "Exit", command = root.quit )
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
	dropdown = ttk.Combobox(tab1b, textvariable = A1_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 0, row = 2, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = A2_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 0, row = 1, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = A3_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 0, row = 0, padx = 1)
	dropdown.lift()

	#Col B
	dropdown = ttk.Combobox(tab1b, textvariable = B1_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 1, row = 2, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = B2_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 1, row = 1, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = B3_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 1, row = 0, padx = 1)
	dropdown.lift()

	#Col C
	dropdown = ttk.Combobox(tab1b, textvariable = C1_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 2, row = 2, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = C2_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 2, row = 1, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = C3_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 2, row = 0, padx = 1)
	dropdown.lift()

	#Col D
	dropdown = ttk.Combobox(tab1b, textvariable = D1_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 3, row = 2, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = D2_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 3, row = 1, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = D3_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 3, row = 0, padx = 1)
	dropdown.lift()
	#Col E
	dropdown = ttk.Combobox(tab1b, textvariable = E1_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 4, row = 2, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = E2_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 4, row = 1, padx = 1)
	dropdown.lift()

	dropdown = ttk.Combobox(tab1b, textvariable = E3_W)
	dropdown['values'] = container_list 
	dropdown.grid(column = 4, row = 0, padx = 1)
	dropdown.lift()

	#Save Button - Calibration 
	save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
	save_w = ttk.Button(tab1b, image = save_button_image, width = 5)
	save_w.grid(column = 2, row = 3)

	#Button

	########################################################################################################




	########################################################################################################
	#Calibrate Containers
	########################################################################################################
	#Drop Down Default Selection
	varpip = StringVar(root, value='')
  
	#Selection 1 - Pipette
	label = ttk.Label(tab3, text='Select a Pipette', font = ('Arial', 15))
	label.grid(column = 0, row = 1, padx = 1)
	dropdown = ttk.Combobox(tab3, textvariable = varpip)
	dropdown['values'] = [ 'p100','p1000' ] # Replace to Global pipette variable
	dropdown.grid(column = 0, row = 2, padx = 1)

	#Drop Down Default Selection
	varcon = StringVar(root, value='')

	#Selection 1 - Containers
	label = ttk.Label(tab3, text='Select a Container', font = ('Arial', 15))
	label.grid(column = 0, row = 3, padx = 1)
	dropdown = ttk.Combobox(tab3, textvariable = varcon)
	dropdown['values'] = [ '96_well','96_tip' ] # Replace to Global pipette variable
	dropdown.grid(column = 0, row = 4, padx = 1)

	#Section 2 - Pipette Movement 

	#Pipette Movement Increments
	#Movement Pad - X Axis
	#Set Image to variable
	xn_button_image = PhotoImage(file="graphic/arrow-left-bold-circle.png") # [ Y Axis Positive ]
	left_b = ttk.Button(tab3, image = xn_button_image, width = 5)
	left_b.grid(column = 1, row = 2)

	#Movement Pad - X Axis
	#Set Image to variable 
	xp_button_image = PhotoImage(file="graphic/arrow-right-bold-circle.png") # [ X Axis Positive ]
	right_b = ttk.Button(tab3, image = xp_button_image, width = 5)
	right_b.grid(column = 3, row = 2)

	#Movement Pad - Y Axis
	#Set Image to variable
	yn_button_image = PhotoImage(file="graphic/arrow-up-bold-circle.png") 
	down_b = ttk.Button(tab3, image = yn_button_image, width = 5)
	down_b.grid(column = 2, row = 1)

	#Movement Pad - Y Axis
	#Set Image to variable
	yp_button_image = PhotoImage(file="graphic/arrow-down-bold-circle.png") 
	up_b = ttk.Button(tab3, image = yp_button_image, width = 5)
	up_b.grid(column = 2, row = 3)


	#Movement Pad - Z Axis [Pipette Movement] Down
	zd_button_image = PhotoImage(file="graphic/arrow-down-bold-circle.png") 
	z_up_b = ttk.Button(tab3, image = zd_button_image, width = 5)
	z_up_b.grid(column = 1, row = 3)

	#Movement Pad - Z Axis [Pipette Movement] UP
	zu_button_image = PhotoImage(file="graphic/arrow-up-bold-circle.png") 
	z_down_b = ttk.Button(tab3, image = zu_button_image, width = 5)
	z_down_b.grid(column = 1, row = 1)

	#Home
	home_image = PhotoImage(file="graphic/home.png") 
	home_b = ttk.Button(tab3, image = home_image, width = 5)
	home_b.grid(column = 2, row = 4)

	#Move to preconfigured 
	pre_home_image = PhotoImage(file="graphic/content-save-settings.png")
	pre_home_b = ttk.Button(tab3, image = pre_home_image, width = 5)
	pre_home_b.grid(column = 3, row = 4)

	#Save Button - Calibration 
	#save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
	save_c = ttk.Button(tab3, image = save_button_image, width = 5)
	save_c.grid(column = 1, row = 4)

	#########################################################################################################
	#Setup Pipette
	#Drop Down Default Selection
	varcon = StringVar(root, value='')
	var_p_a = IntVar()
	var_max_volume = DoubleVar()
	var_min_volume = DoubleVar()
	var_aspirate_speed = DoubleVar()
	var_dispense_speed = DoubleVar()
	s_tip_rack = StringVar(root, value='')
	s_trash = StringVar(root, value='')

	#Selection 1 - Axis
	label = ttk.Label(tab1, text='Select a Axis', font = ('Arial', 12))
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
	label = ttk.Label(tab1, text='Select a max volume', font = ('Arial', 12))
	label.grid(column = 1, row = 2)
	#Scale Bar
	scale_2 = Scale(tab1, from_=0, to=500, resolution = 1, orient="horizontal", variable = var_max_volume)
	scale_2.grid(column = 1, row = 3)

	#Selection 3 - Min Volume
	label = ttk.Label(tab1, text='Select a min volume', font = ('Arial', 12))
	label.grid(column = 1, row = 4)
	#Scale Bar
	scale_3 = Scale(tab1, from_=0, to=500, resolution = 1, orient="horizontal", variable = var_min_volume)
	scale_3.grid(column = 1, row = 5)

	#Selection 3 - aspirate_speed
	label = ttk.Label(tab1, text='Select aspirate speed', font = ('Arial', 12))
	label.grid(column = 1, row = 6)
	#Scale Bar
	scale_2 = Scale(tab1, from_=100, to=600, resolution = 1, orient="horizontal", variable = var_aspirate_speed)
	scale_2.grid(column = 1, row = 7)

	# Separator object
	separator = ttk.Separator(tab1, orient='vertical')
	separator.grid(row=0,column=4, rowspan=10, ipady=140)

	#Selection 4 - dispense_speed
	label = ttk.Label(tab1, text='Select a dispense speed', font = ('Arial', 12))
	label.grid(column = 6, row = 0)
	#Scale Bar
	scale_3 = Scale(tab1, from_=100, to=600, resolution = 1, orient="horizontal", variable = var_dispense_speed)
	scale_3.grid(column = 6, row = 1)

	#Selection 5 - Select a Tip Rack
	label = ttk.Label(tab1, text='Select a Tip Rack', font = ('Arial', 12))
	label.grid(column = 6, row = 2)
	dropdown = ttk.Combobox(tab1, textvariable = s_tip_rack)
	dropdown['values'] = [ '96_tip_p100', '96_tip_p1000'] # Replace to Global pipette variable
	dropdown.grid(column = 6, row = 3)

	#Selection 6 - Select a Bin
	label = ttk.Label(tab1, text='Select a Bin', font = ('Arial', 12))
	label.grid(column = 6, row = 4)
	dropdown = ttk.Combobox(tab1, textvariable = s_trash)
	dropdown['values'] = [ 'trash_p100', 'trash_p1000'] # Replace to Global pipette variable
	dropdown.grid(column = 6, row = 5)

	# Save Button
	save_pip = ttk.Button(tab1, image = save_button_image, width = 5)
	save_pip.grid(column = 6, row = 6)

	# Separator object
	separator = ttk.Separator(tab1, orient='vertical')
	separator.grid(row=0,column=8, rowspan=10, ipady=140)

	#Use Pre-Configured Pipetting in script/database
	label = ttk.Label(tab1, text='Load Pre-Configured:', font = ('Arial', 12))
	label.grid(column = 9, row = 0)

	pre_select_pip = ttk.Button(tab1, image = pre_home_image, width = 5)
	pre_select_pip.grid(column = 10, row = 0)


    #########################################################################################################
    #Calibrate Pipette

	#Selection 1 - Pipette
	label = ttk.Label(tab2, text='Select a Pipette', font = ('Arial', 15))
	label.grid(column = 0, row = 1, padx = 1)
	dropdown = ttk.Combobox(tab2, textvariable = varpip)
	dropdown['values'] = [ 'p100','p1000' ] # Replace to Global pipette variable
	dropdown.grid(column = 0, row = 2, padx = 1)

	#Drop Down Default Selection
	pippos = StringVar(root, value=' ')
	#Selection 2 - Which Selection
	label = ttk.Label(tab2, text='Select a Position', font = ('Arial', 15))
	label.grid(column = 0, row = 3, padx = 1)
	dropdown = ttk.Combobox(tab2, textvariable = pippos)
	dropdown['values'] = [ 'top','bottom', 'blow_out','drop_tip'] # Replace to Global pipette variable
	dropdown.grid(column = 0, row = 4, padx = 1)

	#Pipette Movement Increments
	#Movement Pad - Z Axis [Pipette Movement] Down
	z_up_bp = ttk.Button(tab2, image = zd_button_image, width = 5)
	z_up_bp.grid(column = 1, row = 3)

	#Movement Pad - Z Axis [Pipette Movement] UP 
	z_down_bp = ttk.Button(tab2, image = zu_button_image, width = 5)
	z_down_bp.grid(column = 1, row = 1)

	#Home Button
	home_b = ttk.Button(tab2, image = home_image, width = 5)
	home_b.grid(column = 2, row = 4)

	#Move to preconfigured 
	pre_home_b = ttk.Button(tab2, image = pre_home_image, width = 5)
	pre_home_b.grid(column = 3, row = 4)

	#Save Button - Calibration  
	save_p = ttk.Button(tab2, image = save_button_image, width = 5)
	save_p.grid(column = 1, row = 4)

	root.mainloop() 


#Debugging (Run Graphical Interface without backend code)
graphicalUIcalibrate()