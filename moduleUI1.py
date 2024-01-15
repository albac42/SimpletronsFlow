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


        self
        # Start the main loop
        self.mainloop()

class Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

# Instantiate the App class with default title and size
app = App('Simpletrons - OT', (740, 400))

    


###########################################################################################################

###########################################################################################################
#
# Global Variable 
#
###########################################################################################################
# Remember to verify the custom container exist before adding into this container list to reduce errors

