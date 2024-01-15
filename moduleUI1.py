#Import User Interface Library 
from tkinter import *


#Database
import sqlite3
from sqlite3 import Error

#START UP GUI
from tkinter.ttk import Combobox
import tkinter as tk    
from tkinter import ttk


#Import RE
import re

#Import threading
import threading

#Custom module Imports


## OS Path
import os.path
###########################################################################################################

# Python TK Graphical Interface Note: [Run on Start]
# Note: This Is Only UI Section (If you want to expand or start from scratch use other python script such as
# moduleProtocol, moduleCommands, moduleCalibrate)

###########################################################################################################



###########################################################################################################
#
# Start Up Command
#
###########################################################################################################
#connect()
#create_connection()

###########################################################################################################
#
# Start UI
#
###########################################################################################################
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        self.title(title)
        self.geometry("+{}+{}".format(int(self.winfo_screenwidth()/4 - self.winfo_reqwidth()/4), int(self.winfo_screenheight()/4 - self.winfo_reqheight()/4)))

        notebook = ttk.Notebook(parent)
    
        # Create the menu bar
        s_menu = Menu(self)
        self.config(menu=s_menu)

        # File menu
        file_menu = Menu(s_menu)
        s_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Protocol...", command=self.graphicalUIprotocol)
        file_menu.add_command(label="About", command=self.aboutPage)
        file_menu.add_command(label="Source Code", command=self.open_url_github)
        file_menu.add_command(label="Exit", command=self.quit)

        # Troubleshooting menu
        file2_menu = Menu(s_menu)
        s_menu.add_cascade(label="Troubleshooting", menu=file2_menu)
        file2_menu.add_command(label="Robot Connections Options", command=self.connecton_graphical)
        file2_menu.add_command(label="Start Demo Protocol", command=self.load_demo_protocol)
        file2_menu.add_command(label="Documentation", command=self.open_url_doc)

        # Start the main loop
        self.mainloop()

    def aboutPage(self):
        self.confirmation_box(1)
        # Add your code for the About page here
        pass

    def graphicalUIprotocol(self):
        def __init__(self, root):
            self.root = root

            self.v1 = None
            self.v2 = None
            self.v3 = None
            self.v4 = None
            self.shortcuts_list = None
            self.dropdown_dispense_c = None
            self.dropdown_aspirate_c = None
            self.dropdown_ppip = None
            self.dispense_con = None
            self.well_1 = None
            self.well_2 = None
            self.save_button_image_pro = None
            self.background_image2 = None
            self.background_image3 = None
            self.background3 = None
            self.background2 = None
            self.step = 1
            self.max_step = 1
            self.current_row = 1
            self.current_step_label_v = None

        # Call the graphicalUIprotocol function
        self.graphicalUIprotocol()

    def open_url_github(self):
        # Add your code for opening the GitHub URL here
        pass

    def connecton_graphical(self):
        # Add your code for the Robot Connections Options here
        pass

    def load_demo_protocol(self):
        # Add your code for starting the demo protocol here
        pass

    def open_url_doc(self):
        # Add your code for opening the Documentation URL here
        pass

    def confirmation_box(self, option):
        # Add your code for the confirmation box here
        pass
    # Start the main loop
        self.mainloop()

class Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
    def create widgets():

# Instantiate the App class with default title and size
app = App('Simpletrons - OT', (740, 400))

    


###########################################################################################################

###########################################################################################################
#
# Global Variable 
#
###########################################################################################################
# Remember to verify the custom container exist before adding into this container list to reduce errors

