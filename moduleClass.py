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

# Class Tool Tip
class Tooltip:
    '''
    It creates a tooltip for a given widget as the mouse goes on it.
    Source: 
    http://www.daniweb.com/programming/software-development/
           code/484591/a-tooltip-class-for-tkinter
    '''

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
                # No further checks will be done.

                # TIP:
                # A further mod might automagically augment the
                # wraplength when the tooltip is too high to be
                # kept inside the screen.
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