
print ( "This is the TakeNotes installation process" )
print ( "The time is based on your computer's speed and internet" )
print ( "Started...\n" )

from google_drive_downloader import GoogleDriveDownloader as g

g.download_file_from_google_drive ( file_id = '1vxt6Kq_8llsEiwKvrKqwjkADkxuapRnz', dest_path = 'C:\TakeNotes\TakeNotes_zip.zip', unzip = True )

from os import remove
from os.path import exists
    
remove ( 'C:\TakeNotes\TakeNotes_zip.zip' )

print ( "Making shortcuts..." )

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

print ( "\nCompleted!" )
