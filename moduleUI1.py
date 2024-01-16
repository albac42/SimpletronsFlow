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

import tkinter as tk
from tkinter import ttk
from tkinter import Menu

class App(tk.Tk):
    def __init__(self, title):
        super().__init__()

        self.title(title)
        self.geometry("+{}+{}".format(int(self.winfo_screenwidth()/4 - self.winfo_reqwidth()/4), int(self.winfo_screenheight()/4 - self.winfo_reqheight()/4)))

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

        # Create tabs
        self.notebook = ttk.Notebook(self)

        self.Tab1 = Tab1(self.notebook)
        self.Tab2 = Tab2(self.notebook)

        self.notebook.add(self.Frame1, text='Frame1')
        self.notebook.add(self.Frame2, text='Frame2')
        self.notebook.pack()


        # Start the main loop
        self.mainloop()

    def aboutPage(self):
        self.confirmation_box(1)
        # Add your code for the About page here
        pass

    def graphicalUIprotocol(self):
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.v3 = StringVar()
        self.v4 = StringVar()
        self.shortcuts_list = StringVar()
        self.dropdown_dispense_c = StringVar()
        self.dropdown_aspirate_c = StringVar()
        self.dropdown_ppip = StringVar()
        self.dispense_con = StringVar()
        self.well_1 = StringVar()
        self.well_2 = StringVar()
        self.save_button_image_pro = StringVar()
        self.save_button_image_pro = StringVar()
        self.background_image2 = StringVar()
        self.background_image3 = StringVar()
        self.background3 = StringVar()
        self.background2 = StringVar()
        self.step = 1
        self.max_step = 1
        self.current_row = 1
        self.current_step_label_v = StringVar()

        # Add your code for initializing other variables

        # Create Toplevel window
        proroot = Toplevel(self.root)
        proroot.title("Simpletrons - OT: Protocol Designer")
        proroot.configure(background="#f9f4f2")

        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        positionRight = int(self.root.winfo_screenwidth()/3.5 - windowWidth/3.5)
        positionDown = int(self.root.winfo_screenheight()/3.5 - windowHeight/3.5)
        proroot.geometry("+{}+{}".format(positionRight, positionDown))

        def close_popup():
            proroot.destroy()
            proroot.update()


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

# Instantiate the App class with the default title
app = App('Simpletrons - OT')


class Tab1(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelA = ttk.Label(self, text = "This is on Frame One")
        self.labelA.grid(column=1, row=1)

# Instantiate the App class with default title and size
app = App('Simpletrons - OT', (740, 400))

    


###########################################################################################################

###########################################################################################################
#
# Global Variable 
#
###########################################################################################################
# Remember to verify the custom container exist before adding into this container list to reduce errors

