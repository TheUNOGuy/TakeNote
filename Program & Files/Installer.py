
print ( "Welcome to the TakeNotes installer process!" )
print ( "The app will install to C:\TakeNotes\n" )

import time
import os, shutil

def copy ( src, dst, symlinks = False, ignore = None ):
    
    if not os.path.exists ( dst ):
        
        os.makedirs ( dst )
        
    for item in os.listdir ( src ):
        
        s = os.path.join ( src, item )
        d = os.path.join ( dst, item )
        
        if os.path.isdir ( s ):
            copy ( s, d, symlinks, ignore )
        else:
            if not os.path.exists ( d ) or os.stat ( s ).st_mtime - os.stat ( d ).st_mtime > 1:
                shutil.copy2 ( s, d )


def resource_path ( relative_path ):
    
    try:
        base_path = sys._MEIPASS
        
    except Exception:
        base_path = os.path.abspath ( "." )

    return os.path.join ( base_path, relative_path )

print ( "Started..." )

import zipfile as z
import win32com as w
from os import mkdir

try:
    mkdir ( "C:\TakeNotes" )

except:
    pass

import winshell
from win32com.client import Dispatch
from distutils.dir_util import copy_tree

p = resource_path ( "TakeNotes" )

copy ( p, "C:\TakeNotes")

pathname = winshell.desktop() 
path = os.path.join ( pathname, "TakeNotes.lnk" )

target = r"C:\TakeNotes\TakeNotes.exe"
wDir = r"C:\TakeNotes\TakeNotes.exe"
icon = r"C:\TakeNotes\TakeNotes.exe"

shell = Dispatch ( 'WScript.Shell' )

shortcut = shell.CreateShortCut ( path )
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

from pathlib import Path

home = str ( Path.home() )
path = "AppData\Roaming\Microsoft\Windows\Start Menu\Programs"

path = os.path.join ( home, path )
path = os.path.join ( path, "TakeNotes.lnk" )

shortcut = shell.CreateShortCut ( path )
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

print ( "Completed!" )
