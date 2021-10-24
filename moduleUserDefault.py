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

#Custom module Imports
from moduleContainers import *
from moduleCommands import *
from moduleCalibrate import *
from modulePipetting import *

###########################################################################################################