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
