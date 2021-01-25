

print ( "This is the TakeNotes Installation process!" )
print ( "This app will install to C:\TakeNotes\n")
print ( "Started..." )

from google_drive_downloader import GoogleDriveDownloader as g

g.download_file_from_google_drive ( file_id = '1wjDnMEu4cweg6-ufEBIZuishf5V6bNNH', dest_path = 'C:\TakeNotes\TakeNotes_zip.zip', unzip = True )

from os import remove
from os.path import exists
    
remove ( 'C:\TakeNotes\TakeNotes_zip.zip' )

import winshell
from win32com.client import Dispatch
from distutils.dir_util import copy_tree
from os.path import join as jon

pathname = winshell.desktop() 
path = jon ( pathname, "TakeNotes.lnk" )

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

path = jon ( home, path )
path = jon ( path, "TakeNotes.lnk" )

shortcut = shell.CreateShortCut ( path )
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

try:
    from os import mkdir

    home = str ( Path.home() )
    path = 'AppData\Local\TN'
    path = jon ( home, path )
    mkdir ( path )

except:
    pass

print ( "-Completed!" )
