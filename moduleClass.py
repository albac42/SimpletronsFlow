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

#Import threading
import threading

#Custom module Imports
# from moduleContainers import *
from moduleCommands import *
# from moduleCalibrate import *
# from modulePipetting import *
from moduleProtocol import *

## OS Path
import os.path
import os
from tkinter import filedialog
import webbrowser

###########################################################################################################
#
# Global Graphical Function - 
###########################################################################################################

# Class Tool Tip
class Tooltip:
    """
    Tool tip Generation

    """

    def __init__(self, widget,
                 *,
                 bg='#FFFFEA',
                 pad=(5, 3, 5, 3),
                 text='widget info',
                 waittime=400,
                 wraplength=250):

        self.waittime = waittime
        self.wraplength = wraplength
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.onEnter)
        self.widget.bind("<Leave>", self.onLeave)
        self.widget.bind("<ButtonPress>", self.onLeave)
        self.bg = bg
        self.pad = pad
        self.id = None
        self.tw = None

    def onEnter(self, event=None):
        self.schedule()

    def onLeave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.show)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def show(self):
        def tip_pos_calculator(widget, label,
                               *,
                               tip_delta=(10, 5), pad=(5, 3, 5, 3)):

            w = widget

            s_width, s_height = w.winfo_screenwidth(), w.winfo_screenheight()

            width, height = (pad[0] + label.winfo_reqwidth() + pad[2],
                             pad[1] + label.winfo_reqheight() + pad[3])

            mouse_x, mouse_y = w.winfo_pointerxy()

            x1, y1 = mouse_x + tip_delta[0], mouse_y + tip_delta[1]
            x2, y2 = x1 + width, y1 + height

            x_delta = x2 - s_width
            if x_delta < 0:
                x_delta = 0
            y_delta = y2 - s_height
            if y_delta < 0:
                y_delta = 0

            offscreen = (x_delta, y_delta) != (0, 0)

            if offscreen:

                if x_delta:
                    x1 = mouse_x - tip_delta[0] - width

                if y_delta:
                    y1 = mouse_y - tip_delta[1] - height

            offscreen_again = y1 < 0  # out on the top

            if offscreen_again:
                y1 = 0

            return x1, y1

        bg = self.bg
        pad = self.pad
        widget = self.widget

        # creates a toplevel window
        self.tw = tk.Toplevel(widget)

        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)

        win = tk.Frame(self.tw,
                       background=bg,
                       borderwidth=0)
        label = tk.Label(win,
                          text=self.text,
                          justify=tk.LEFT,
                          background=bg,
                          relief=tk.SOLID,
                          borderwidth=0,
                          wraplength=self.wraplength)

        label.grid(padx=(pad[0], pad[2]),
                   pady=(pad[1], pad[3]),
                   sticky=tk.NSEW)
        win.grid()

        x, y = tip_pos_calculator(widget, label)

        self.tw.wm_geometry("+%d+%d" % (x, y))

    def hide(self):
        tw = self.tw
        if tw:
            tw.destroy()
        self.tw = None
    '''
    It creates a tooltip for a given widget as the mouse goes on it.
    Source: 
    http://www.daniweb.com/programming/software-development/
           code/484591/a-tooltip-class-for-tkinter
    '''


###########################################################################################################
#
# Popup Window [If You need create popup windows use below template]
#
###########################################################################################################

def confirmation_box_v2(text):
    """
    Pop Up Windows Creation
    """
    newWindow = Tk()

    newWindow.title("Simpletrons - OT")
    #newWindow.geometry("200x60")

    #Set Window Location
    windowWidth = newWindow.winfo_reqwidth() 
    windowHeight = newWindow.winfo_reqheight()
    positionRight = int(newWindow.winfo_screenwidth()/4 - windowWidth/4)
    positionDown = int(newWindow.winfo_screenheight()/4 - windowHeight/4)
    newWindow.geometry("+{}+{}".format(positionRight, positionDown))


    def close_popup():
        newWindow.destroy()
        #newWindow.update()

    def close_popup_protocol_1():
        """Delete Row"""
        count = read_row(custom_protocol)
        deleteRecord(custom_protocol, count)    

    print(text)
    v_text_input = StringVar()
    label = Label(newWindow, textvariable=v_text_input, font = ('Arial', 15))
    label.grid(column = 0, row = 0, sticky="NW")
    v_text_input.set(text)
    save_button_image = PhotoImage(file="graphic/content-save-outline.png") 
    save_w = ttk.Button(newWindow, text='OK', width = 5, command = close_popup)
    save_w.grid(column = 0, row = 1)



def confirmation_box(variable):
    """
    Pop Up Windows Creation
    """

    version = 'Version: Private Alpha 1.5'

    newWindow = Tk()

    newWindow.title("Simpletrons - OT")
    #newWindow.geometry("200x60")

    #Set Window Location
    windowWidth = newWindow.winfo_reqwidth() 
    windowHeight = newWindow.winfo_reqheight()
    positionRight = int(newWindow.winfo_screenwidth()/4 - windowWidth/4)
    positionDown = int(newWindow.winfo_screenheight()/4 - windowHeight/4)
    newWindow.geometry("+{}+{}".format(positionRight, positionDown))


    def close_popup():
        newWindow.destroy()
        #newWindow.update()

    def close_popup_protocol_1():
        """Delete Row"""
        count = read_row(custom_protocol)
        deleteRecord(custom_protocol, count)


    if variable == 1:
        newWindow.geometry("250x60")
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
        label = Label(newWindow, text='Successfully Save \n Calibration Container', font = ('Arial', 9))
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

    elif variable == 11:
        newWindow.geometry("140x60")
        label = Label(newWindow, text='Error: Check Well Input', font = ('Arial', 9))
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
#
# Connection To Robot [Pop Up]
#
###########################################################################################################

def connecton_graphical():
    """ Connection UI"""
    """ """
    conroot = Tk()

    conroot.title("Simpletrons - OT: Protocol - Connection")

    #Set Window Location
    windowWidth = conroot.winfo_reqwidth() 
    windowHeight = conroot.winfo_reqheight()
    positionRight = int(conroot.winfo_screenwidth()/4 - windowWidth/4)
    positionDown = int(conroot.winfo_screenheight()/4 - windowHeight/4)
    conroot.geometry("+{}+{}".format(positionRight, positionDown))

    def close_popup():
        conroot.destroy()
        #conroot.update()
    ###
    s_menu = Menu(conroot)
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
    
    def home_treading():
        print("Starting Threading: Home")
        threading.Thread(target=home_robot).start()

    save_step = ttk.Button(conroot, text = 'Home', width = 6, command = home_treading)
    save_step.grid(column = 0, row = 5)

#Start Protocol
def start_protocol_ui_demo(db_file):

    con_pro_ui_root = Tk()

    wraplength = 250

    con_pro_ui_root.title("Simpletrons - OT: Start Protocol")

    con_pro_ui_root.lift()
    con_pro_ui_root. attributes("-topmost", True)

    windowWidth = con_pro_ui_root.winfo_reqwidth() 
    windowHeight = con_pro_ui_root.winfo_reqheight()
    positionRight = int(con_pro_ui_root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(con_pro_ui_root.winfo_screenheight()/2 - windowHeight/2)
    con_pro_ui_root.geometry("+{}+{}".format(positionRight, positionDown))



    def close_popup():
        con_pro_ui_root.destroy()
        con_pro_ui_root.update()
    ###

    label = ttk.Label(con_pro_ui_root, text = 'Start Protocol:')
    label.grid(column = 0, row = 1)

    def send_command_start_protocol():
        threading.Thread(target=start_protocol_temp(db_file)).start()
    
    start_step = ttk.Button(con_pro_ui_root, text = 'Start', width = 8, command = send_command_start_protocol)
    start_step.grid(column = 0, row = 2)
    Tooltip(start_step, text='Start Protocol', wraplength=wraplength)

    stop_step = ttk.Button(con_pro_ui_root, text = 'STOP', width = 6, command = resume_robot)
    stop_step.grid(column = 1, row = 2)
    Tooltip(stop_step, text='Stop Protocol - Note Will Close Application', wraplength=wraplength)

def load_demo_protocol():
    '''
    Setup Demo Environment 
    '''
    deleteTable("custom_protocol")
    deleteTable("custom_pipette")
    deleteTable("custom_workspace")
        
    test_save_data_demo()
    start_protocol_ui_demo('database/data.db')


def import_protocol():

    con_pro_ui_root = Tk()

    wraplength = 250

    con_pro_ui_root.title("Simpletrons - OT: Start Protocol")

    con_pro_ui_root.lift()
    con_pro_ui_root. attributes("-topmost", True)

    windowWidth = con_pro_ui_root.winfo_reqwidth() 
    windowHeight = con_pro_ui_root.winfo_reqheight()
    positionRight = int(con_pro_ui_root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(con_pro_ui_root.winfo_screenheight()/2 - windowHeight/2)
    con_pro_ui_root.geometry("+{}+{}".format(positionRight, positionDown))



    def close_popup():
        con_pro_ui_root.destroy()
        con_pro_ui_root.update()

    con_pro_ui_root.withdraw() #use to hide tkinter window

    currdir = os.getcwd()+str("/export/")
    tempdir = filedialog.askopenfilename(parent=con_pro_ui_root, initialdir=currdir, title='Please select a db', filetypes = (("db files","*.db"),("all files","*.*")))

    if len(tempdir) > 0:
        print ("You chosen %s" % tempdir)


    start_protocol_ui_demo(tempdir)

    con_pro_ui_root.destroy()
    try:
        con_pro_ui_root.update()
    except:
        pass

def open_url_github():
    webbrowser.open("https://github.com/skydivercactus/simpletrons")

def open_url_doc():
    webbrowser.open("https://github.com/skydivercactus/simpletrons/wiki")