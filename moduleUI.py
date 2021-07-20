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

#Custom moudle Imports
from moduleContainers import *
from moduleCommands import *
from moduleCalibrate import *
from moduleLink import *

version = 'Version: Private Alpha 0.1'

#Global Variable
container_list = [ '', 'trash-box','tiprack-10ul', 'tiprack-200ul', 'tiprack-1000ul', '96-flat', '96-PCR-flat', '96-PCR-tall',  '96-deep-well']
loaded_pipette_list = ['','']
loaded_container_type = []
loaded_containers = []
count_CT = 0
count_CTT = 0
count_C = 0



#load_dd_container()
#connect()
create_connection('database/data.db')

# Start GUI
root = Tk()
root.title('Simpletrons - OT')


def update_containers_list_type():

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
	global loaded_containers
	global count_CT

	loaded_containers.append(count_CT)
	loaded_containers[count_CT]= name
	count_CT = count_CT + 1

def update_pipette(name, num):

	loaded_pipette_list[num]= name


###########################################################################################################
#
# Function Link - Move to Module After Testing *TO DO*
#
###########################################################################################################
def save_pip_action():
	pip = varpip.get()
	print(pip)
	pos = pippos.get()
	print(pos)
	saveCalibration(pip, pos)
	print('Command Sucessfull Saved Calibration')

def move_pip_action_up():
	pip = varpip.get()
	calibrationControlPlugger(pip, z_up)

def move_pip_action_down():
	pip = varpip.get()
	calibrationControlPlugger(pip, z_down)

def move_prepip_action():
	pip = varpip.get()
	moveDefaultLocation(pip)
	print('Scuessfully Moved To Saved Position')

#Save Custom Pipette
def action_save_pip():
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

	tiprack = s_tip_rack.get()
	trash = s_trash.get()

	print(max_vol)
	print(min_vol)
	print(asp_speed)
	print(dis_speed)

	print(tiprack)
	print(trash)

	loadpipette (axis, max_vol, min_vol, asp_speed, dis_speed, tiprack, trash)
	print(loaded_pipette_list)


def load_pre_workspace(): #For Testing
	pass


def load_pre_pip(): #For Testing

	loadpipette ('a', 1000, 100, 800, 1200, 'B1_tiprack-1000ul', 'A2_trash-box')
	update_pipette('pipette_a', 1)
	loadpipette ('b', 1000, 100, 800, 1200, 'B2_tiprack-1000ul', 'A2_trash-box')
	update_pipette('pipette_b', 0)
	
#Reference
#load_container(name, location, container)
def setup_workspace():
	#Reset Counter
	global count_C
	global count_CT
	count_CT = 0
	#count_C = 0

	loaded_containers.clear()

	if A1_W.get() != '':
		print('Entry Found in A1')
		AA = 'A1_'+str(A1_W.get())
		BB = A1_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'A1', BB)
	if A2_W.get() != '':
		print('Entry Found in A2')
		AA = 'A2_'+str(A2_W.get())
		BB = A2_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'A2', BB)
	if A3_W.get() != '':
		print('Entry Found in A3')
		AA = 'A3_'+str(A3_W.get())
		BB = A3_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'A3', BB)
	if B1_W.get() != '':
		print('Entry Found in B1')
		AA = 'B1_'+str(B1_W.get())
		BB = B1_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'B1', BB)
	if B2_W.get() != '':
		print('Entry Found in B2')
		AA = 'B2_'+str(B2_W.get())
		BB = B2_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'B2', BB)
	if B3_W.get() != '':
		print('Entry Found in B3')
		AA = 'B3_'+str(B3_W.get())
		BB = B3_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'B3', BB)
	if C1_W.get() != '':
		print('Entry Found in C1')
		AA = 'C1_'+str(C1_W.get())
		BB = C1_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'C1', BB)
	if C2_W.get() != '':
		print('Entry Found in C2')
		AA = 'C2_'+str(C2_W.get())
		BB = C2_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'C2', BB)
	if C3_W.get() != '':
		print('Entry Found in C3')
		AA = 'C3_'+str(C3_W.get())
		BB = C3_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'C3', BB)
	if D1_W.get() != '':
		print('Entry Found in D1')
		AA = 'D1_'+str(D1_W.get())
		BB = D1_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'D1', BB)
	if D2_W.get() != '':
		print('Entry Found in D2')
		AA = 'D2_'+str(D2_W.get())
		BB = D2_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'D2', BB)
	if D3_W.get() != '':
		print('Entry Found in D3')
		AA = 'D3_'+str(D3_W.get())
		BB = D3_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'D3', BB)
	if E1_W.get() != '':
		print('Entry Found in E1')
		AA = 'E1_'+str(E1_W.get())
		BB = E1_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'E1', BB)
	if E2_W.get() != '':
		print('Entry Found in E2')
		AA = 'E2_'+str(E2_W.get())
		BB = E2_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'E2', BB)
	if E3_W.get() != '':
		print('Entry Found in E3')
		AA = 'E3_'+str(E3_W.get())
		BB = E3_W.get()
		print(AA)

		update_containers_list(AA)
		load_container(AA, 'E3', BB)
	#Update Loaded in Workspaec Container List
	update_containers_list_type()
	print(loaded_containers)


#Update Tip Rack List
def update_dropdown_tip_rack():
    list = loaded_containers
    dropdown_tip_rack['values'] = list	

#Update Tip Rack List
def update_dropdown_trash():
    list = loaded_containers
    dropdown_trash['values'] = list


def update_dropdown_pip():
    list = loaded_pipette_list
    dropdown_cpip['values'] = list	

def update_dropdown_pip_c():
    list = loaded_pipette_list
    dropdown_varpip_c['values'] = list	


def list_containers():

	return 

def graphicalUIprotocol(): # Start Graphical Protocal Interface
	pass

def aboutPage():
	confirmation_box(1)
	pass



###########################################################################################################
#
# Containers Creation UI
#
###########################################################################################################

def confirmation_box(variable):

	global version

	newWindow = Toplevel(root)

	newWindow.title("Simpletrons - OT")
	newWindow.geometry("200x60")


	if variable == 1:
		label = Label(newWindow, text='Simpletrons - OT', font = ('Arial', 15))
		label.grid(column = 0, row = 0, sticky="NW")
		label2 = Label(newWindow, text=version, font = ('Arial', 15))
		label2.grid(column = 0, row = 1, sticky="NW")
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

#Save Button - Save Workspace 
save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
save_w = ttk.Button(tab1b, image = save_button_image, width = 5, command = setup_workspace)
save_w.grid(column = 2, row = 3)

#Save Button - Load Pre-Configured Workspace
pree_home_image = PhotoImage(file="graphic/content-save-settings.png")
save_w = ttk.Button(tab1b, image = pree_home_image, width = 5, command = load_pre_workspace)
save_w.grid(column = 3, row = 3)

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
dropdown_varpip_c = ttk.Combobox(tab3, textvariable = varpip, postcommand = update_dropdown_pip_c)
#dropdown['values'] = [ 'p100','p1000' ] # Replace to Global pipette variable
dropdown_varpip_c.grid(column = 0, row = 2, padx = 1)

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
var_max_volume = IntVar()

label = ttk.Label(tab1, text='Select a max volume', font = ('Arial', 12))
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

label = ttk.Label(tab1, text='Select a min volume', font = ('Arial', 12))
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

label = ttk.Label(tab1, text='Select aspirate speed', font = ('Arial', 12))
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

label = ttk.Label(tab1, text='Select a dispense speed', font = ('Arial', 12))
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
label = ttk.Label(tab1, text='Select a Tip Rack', font = ('Arial', 12))
label.grid(column = 6, row = 0)
dropdown_tip_rack = ttk.Combobox(tab1, textvariable = s_tip_rack, postcommand = update_dropdown_tip_rack)
#dropdown['values'] = loaded_containers # Replace to Global pipette variable
dropdown_tip_rack.grid(column = 6, row = 1)

#Selection 6 - Select a Bin
label = ttk.Label(tab1, text='Select a Bin', font = ('Arial', 12))
label.grid(column = 6, row = 2)
dropdown_trash = ttk.Combobox(tab1, textvariable = s_trash, postcommand = update_dropdown_trash)
#dropdown['values'] = loaded_containers # Replace to Global pipette variable
dropdown_trash.grid(column = 6, row = 3)

# Save Button
save_pip = ttk.Button(tab1, image = save_button_image, width = 5, command = action_save_pip)
save_pip.grid(column = 6, row = 4)

# Separator object
separator = ttk.Separator(tab1, orient='vertical')
separator.grid(row=0,column=8, rowspan=10, ipady=180)

#Use Pre-Configured Pipetting in script/database
label = ttk.Label(tab1, text='Load Pre-Configured:', font = ('Arial', 12))
label.grid(column = 6, row = 5)

pre_select_pip = ttk.Button(tab1, image = pre_home_image, width = 5, command = load_pre_pip)
pre_select_pip.grid(column = 6, row = 6)


#########################################################################################################
#Calibrate Pipette

#Selection 1 - Pipette
label = ttk.Label(tab2, text='Select a Pipette', font = ('Arial', 15))
label.grid(column = 0, row = 1, padx = 1)
dropdown_cpip = ttk.Combobox(tab2, textvariable = varpip, postcommand = update_dropdown_pip)
#dropdown_cpip['values'] = [ 'p100','p1000' ] # Replace to Global pipette variable
dropdown_cpip.grid(column = 0, row = 2, padx = 1)

#Drop Down Default Selection
pippos = StringVar(root, value=' ')
#Selection 2 - Which Selection
label = ttk.Label(tab2, text='Select a Position', font = ('Arial', 15))
label.grid(column = 0, row = 3, padx = 1)
dropdown_cpos = ttk.Combobox(tab2, textvariable = pippos)
dropdown_cpos['values'] = [ 'top','bottom', 'blow_out','drop_tip']
dropdown_cpos.grid(column = 0, row = 4, padx = 1)

#Pipette Movement Increments
#Movement Pad - Z Axis [Pipette Movement] Down
z_up_bp = ttk.Button(tab2, image = zd_button_image, width = 5, command = move_pip_action_up)
z_up_bp.grid(column = 1, row = 3)

#Movement Pad - Z Axis [Pipette Movement] UP 
z_down_bp = ttk.Button(tab2, image = zu_button_image, width = 5, command = move_pip_action_down)
z_down_bp.grid(column = 1, row = 1)

#Home Button
home_b = ttk.Button(tab2, image = home_image, width = 5, command = move_pip_action_home)
home_b.grid(column = 2, row = 4)

#Move to preconfigured 
pre_home_b = ttk.Button(tab2, image = pre_home_image, width = 5, command = move_prepip_action)
pre_home_b.grid(column = 3, row = 4)

#Save Button - Calibration  
save_p = ttk.Button(tab2, image = save_button_image, width = 5, command = save_pip_action)
save_p.grid(column = 1, row = 4)

root.mainloop() 


#Debugging (Run Graphical Interface without backend code)
#graphicalUIcalibrate()