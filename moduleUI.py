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
	tabControl.add(tab1, text ='Step 1 Custom Containers')
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
	label = ttk.Label(tab3, text='Select a pipette', font = ('Arial', 15))
	label.grid(column = 0, row = 1, padx = 1)
	dropdown = ttk.Combobox(tab3, textvariable = varpip)
	dropdown['values'] = [ 'p100','p1000' ] # Replace to Global pipette variable
	dropdown.grid(column = 0, row = 2, padx = 1)

	#Drop Down Default Selection
	varcon = StringVar(root, value=' ')

	#Selection 1 - Containers
	label = ttk.Label(tab3, text='Select a containers', font = ('Arial', 15))
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



	#Save Button
	save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
	save_c = ttk.Button(tab3, image = save_button_image, width = 5)
	save_c.grid(column = 1, row = 4)


	#########################################################################################################
	ttk.Label(tab1,
    	      text ="Lets dive into the\
        	  world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)



    #########################################################################################################

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


	#Movement Pad - Z Axis [Pipette Movement] Down
	#zd_button_image = PhotoImage(file="graphic/arrow-down-bold-circle.png") 
	z_up_bp = ttk.Button(tab2, image = zd_button_image, width = 5)
	z_up_bp.grid(column = 1, row = 3)

	#Movement Pad - Z Axis [Pipette Movement] UP
	#zu_button_image = PhotoImage(file="graphic/arrow-up-bold-circle.png") 
	z_down_bp = ttk.Button(tab2, image = zu_button_image, width = 5)
	z_down_bp.grid(column = 1, row = 1)
  

	#Movement Pad - Z Axis [Pipette Movement] UP
	#zu_button_image = PhotoImage(file="graphic/arrow-up-bold-circle.png") 
	save_p = ttk.Button(tab2, image = save_button_image, width = 5)
	save_p.grid(column = 1, row = 4)

	root.mainloop() 


#Debugging (Run Graphical Interface without backend code)
graphicalUI()