#Import User Interface Library 
from tkinter import *

#START UP GUI
from tkinter.ttk import Combobox
import tkinter as tk    
from tkinter import ttk


	



# Create a window
def graphicalUI():
	root = Tk()
	root.title('Simpletrons - OT')

	tabControl = ttk.Notebook(root)
	tab1 = ttk.Frame(tabControl)
	tab2 = ttk.Frame(tabControl)

  
	tabControl.add(tab1, text ='Calibration')
	tabControl.add(tab2, text ='Pipette')
	#tabControl.add()


	tabControl.pack(expand = 1, fill ="both")
	#tabControl.grid(column = 3, row = 1, padx = 1)


	########################################################################################################
	#Drop Down Selection
	varpip = StringVar(root, value='select a pipette')
  
	#Selection 1 - Pipette
	label = ttk.Label(tab1, text='Select which pipette to calibrate with', font = ('Arial', 15))
	label.grid(column = 0, row = 1, padx = 1)
	dropdown = ttk.Combobox(tab1, textvariable = varpip)
	dropdown['values'] = [ 'p100','p1000' ]
	dropdown.grid(column = 0, row = 2, padx = 1)

	#Section 2 - Pipette Movement 

	#Pipette Movement Increaments

	#Movement Pad - X Axis
	#Set Image to variable
	left_button = PhotoImage(file="graphic/arrow-left-bold-circle.png") 
	#left_b = ttk.Label(tab1, image=left_button)
	left_b = ttk.Button(tab1, image = left_button)
	left_b.grid(column = 1, row = 2, padx = 1)

	#Movement Pad - X Axis
	#Set Image to variable
	right_button = PhotoImage(file="graphic/arrow-right-bold-circle.png") 
	#left_b = ttk.Label(tab1, image=left_button)
	right_b = ttk.Button(tab1, image = right_button)
	right_b.grid(column = 3, row = 2, padx = 1)

	#Movement Pad - Y Axis
	#Set Image to variable
	right_button = PhotoImage(file="graphic/arrow-right-bold-circle.png") 
	#left_b = ttk.Label(tab1, image=left_button)
	right_b = ttk.Button(tab1, image = right_button)
	right_b.grid(column = 3, row = 2, padx = 1)

	#Movement Pad - Y Axis
	#Set Image to variable
	right_button = PhotoImage(file="graphic/arrow-right-bold-circle.png") 
	#left_b = ttk.Label(tab1, image=left_button)
	right_b = ttk.Button(tab1, image = right_button)
	right_b.grid(column = 3, row = 2, padx = 1)








	#Save Button



	#########################################################################################################
	ttk.Label(tab2,
    	      text ="Lets dive into the\
        	  world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
  
	root.mainloop() 


#Debugging (Run Graphical Interface without backend code)
graphicalUI()