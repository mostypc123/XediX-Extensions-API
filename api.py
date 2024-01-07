import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webview
from tkinter import filedialog
import subprocess
from tkinter import colorchooser # import colorchooser module
from tkinter import font # import font module
from tkinter import *
import re
from tkinter.font import Font
import sqlite3
from tkterminal import Terminal
from idlelib.percolator import Percolator
import pyperclip
from idlelib.colorizer import ColorDelegator as ic
import os
import webbrowser
import xedix
def sh_add(cdgext, name):
    if name in xedix.text.get(2.0):
        Percolator(xedix.text).insertfilter(cdgext)
def window_add(scrname):
            window = tk.Tk(screenName = "XediX Extension: "+scrname)
            window.pack()
def menu_add_mainwindow(name):
    xedix.root.config(menu=xedix.menu)
    new_menu = tk.Menu(master = xedix.root, name=name)
    def menu_mainwindow_add_command(command, label):
        new_menu.add_command(label=label, command=command)
