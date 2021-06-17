#Import User Interface Library 
from tkinter import *

#START UP GUI
from tkinter.ttk import Combobox
import tkinter as tk    
from tkinter import ttk

from opentrons import robot, containers, instruments
import opentrons
from moduleContainers import *



load_dd_container()
#connect()

def list_containers():




	return 


#Update Value 


# Create a window
def graphicalUI():
	root = Tk()
	root.title('Simpletrons - OT')

	#Tab Creation
	tabControl = ttk.Notebook(root)
	tab1 = ttk.Frame(tabControl)
	tab2 = ttk.Frame(tabControl)
	tab3 = ttk.Frame(tabControl)

  	#Tab Header Name
	tabControl.add(tab1, text ='Step 1 Containers/Pipette Setup')
	tabControl.add(tab2, text ='Step 2 Calibrate Pipette')
	tabControl.add(tab3, text ='Step 3 Calibrate Containers')
	#tabControl.add(tab4, text ='Step 3 Protocol Programmer')
	#tabControl.add(tab5, text ='Step 4 Start Protocol')

	tabControl.pack(expand = 1, fill ="both")
	#tabControl.grid(column = 3, row = 1, padx = 1)


	########################################################################################################
	#Drop Down Default Selection
	varpip = StringVar(root, value=' ')
  
	#Selection 1 - Pipette
	label = ttk.Label(tab3, text='Select a Pipette', font = ('Arial', 15))
	label.grid(column = 0, row = 1, padx = 1)
	dropdown = ttk.Combobox(tab3, textvariable = varpip)
	dropdown['values'] = [ 'p100','p1000' ] # Replace to Global pipette variable
	dropdown.grid(column = 0, row = 2, padx = 1)

	#Drop Down Default Selection
	varcon = StringVar(root, value=' ')

	#Selection 1 - Containers
	label = ttk.Label(tab3, text='Select a Container', font = ('Arial', 15))
	label.grid(column = 0, row = 3, padx = 1)
	dropdown = ttk.Combobox(tab3, textvariable = varcon)
	dropdown['values'] = [ 'test_c','test_b' ] # Replace to Global pipette variable
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
	save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
	save_c = ttk.Button(tab3, image = save_button_image, width = 5)
	save_c.grid(column = 1, row = 4)


	#########################################################################################################
	# #Drop Down Default Selection
	# varcon = StringVar(root, value=' ')
	# var_p_a = DoubleVar()
	# #Selection 1 - Containers
	# label = ttk.Label(tab1, text='Select a Axis', font = ('Arial', 15))
	# label.grid(column = 0, row = 0, padx = 1)
	# scale_1 = ttk.Scale(tab1, from_=0, to=42, orient="horizontal", variable = var_p_a)
	# #dropdown['values'] = [ 'test_c','test_b' ] # Replace to Global pipette variable
	# scale_1.grid(column = 1, row = 0, padx = 1)
	# p_value = ttk.Label(tab1, text="0" )

    #########################################################################################################
    #TAB

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
	#zd_button_image = PhotoImage(file="graphic/arrow-down-bold-circle.png") 
	z_up_bp = ttk.Button(tab2, image = zd_button_image, width = 5)
	z_up_bp.grid(column = 1, row = 3)

	#Movement Pad - Z Axis [Pipette Movement] UP
	#zu_button_image = PhotoImage(file="graphic/arrow-up-bold-circle.png") 
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
graphicalUI()