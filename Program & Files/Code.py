
'''
Files have not beeen licensed. Free for use.

Made by the TheUNOGuy ( Registered name in GitHub )

Free to contribute,
Pull requests can be given by anyone!
'''

import wx
import wx.adv
from encrypt import *
from sys import argv
from pyautogui import hotkey
from datetime import datetime

pathname = ''

def checkDarkTheme ( self ):

    with open ( 'C:\TakeNotes\Files\Storage.txt', 'r' ) as theme:

        checkTheme = theme.read()

        if checkTheme == '1':

            self.text_ctrl.SetBackgroundColour ( wx.BLACK )
            self.text_ctrl.SetForegroundColour ( wx.WHITE )

def addpath ( self, path ):

    return "File: " + path

def writing ( self, path ):
    
    text = self.text_ctrl.GetValue()
    
    with open ( path, 'r+' ) as f:
        
        deleteContent ( f )
        text.replace ( "'", "" )
        f.write ( text )
        f.close()
        

def resetPath():
    
    global pathname
    
    pathname = ''

def deleteContent ( pfile ):

    pfile.seek ( 0 )
    pfile.truncate()
    pfile.seek ( 0 ) 

    return pfile

class MyFrame ( wx.Frame ):
    
    def __init__( self ):
        
        super().__init__ ( parent = None, title = 'TakeNotes', size = ( 800, 500 ) )
        panel = wx.Panel ( self )

        self.SetIcon ( wx.Icon ( "C:\TakeNotes\Icon\Icon.png" ) )
        
        sizer = wx.BoxSizer ( wx.VERTICAL ) 
        self.text_ctrl = wx.TextCtrl ( panel, pos = ( 0, 0 ), style = wx.TE_MULTILINE | wx.HSCROLL | wx.TE_RICH )
        sizer.Add ( self.text_ctrl, 1, wx.ALL | wx.EXPAND, 1 )

        checkDarkTheme ( self )

        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusWidths ( [ 600, 100 ] )

        today = datetime.today()

        date = str ( today.strftime ( "%B %d, %Y" ) )
        self.statusbar.SetStatusText ( date, 1 )
                
        panel.SetSizer ( sizer )   
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        menubar.Append ( fileMenu, '&File' )
        
        m0 = fileMenu.Append ( wx.ID_NEW, 'New' )
        self.Bind ( wx.EVT_MENU, self.OnNew, m0 )
        
        fileMenu.AppendSeparator()
        
        m1 = fileMenu.Append ( wx.ID_SAVE, 'Save' )
        self.Bind ( wx.EVT_MENU, self.OnSave, m1 )
        
        m4 = fileMenu.Append ( wx.ID_SAVEAS, 'Save as...' )
        self.Bind ( wx.EVT_MENU, self.OnSaveAs, m4 )
        
        m3 = fileMenu.Append ( wx.ID_OPEN, 'Open...' )
        self.Bind ( wx.EVT_MENU, self.OnOpen, m3 )
        
        fileMenu.AppendSeparator()
        
        m2 = fileMenu.Append ( wx.ID_EXIT, 'Quit' )
        self.Bind ( wx.EVT_MENU, self.OnQuit, m2 )
        self.Bind ( wx.EVT_CLOSE, self.OnExit )
        
        editMenu = wx.Menu()
        menubar.Append ( editMenu, '&Edit' )
        
        c1 = editMenu.Append ( wx.ID_CUT, 'Cut' )
        self.Bind ( wx.EVT_MENU, self.OnCut, c1 )
        
        c2 = editMenu.Append ( wx.ID_COPY, 'Copy' )
        self.Bind ( wx.EVT_MENU, self.OnCopy, c2 )
        
        c3 = editMenu.Append ( wx.ID_PASTE, 'Paste' )
        self.Bind ( wx.EVT_MENU, self.OnPaste, c3 )
        
        editMenu.AppendSeparator()
        
        e1 = editMenu.Append ( wx.ID_UNDO, 'Undo' )
        self.Bind ( wx.EVT_MENU, self.OnUndo, e1 )
        
        e3 = editMenu.Append ( wx.ID_DELETE, 'Delete' )
        self.Bind ( wx.EVT_MENU, self.OnDelete, e3 )
        
        e2 = editMenu.Append ( wx.ID_SELECTALL, 'Select All' )
        self.Bind ( wx.EVT_MENU, self.OnSelectAll, e2 )

        editMenu.AppendSeparator()

        e4 = editMenu.Append ( wx.ID_ANY, 'Insert Date/Time' )
        self.Bind ( wx.EVT_MENU, self.onGetTime, e4 )

        enMenu = wx.Menu()
        menubar.Append ( enMenu, 'Encryption' )

        en1 = enMenu.Append ( wx.ID_ANY, 'Encryption Info' )
        self.Bind ( wx.EVT_MENU, self.OnHowEncrypt, en1 )

        enMenu.AppendSeparator()

        en2 = enMenu.Append ( wx.ID_ANY, 'Encrypt file' )
        self.Bind ( wx.EVT_MENU, self.OnEncrypt, en2 )

        en3 = enMenu.Append ( wx.ID_ANY, 'Decrypt file' )
        self.Bind ( wx.EVT_MENU, self.OnDecrypt, en3 )

        enMenu.AppendSeparator()

        en4 = enMenu.Append ( wx.ID_ANY, 'Forgot Pin' )
        self.Bind ( wx.EVT_MENU, self.OnForgot, en4 )

        viewMenu = wx.Menu()
        menubar.Append ( viewMenu, '&View' )

        f1 = viewMenu.Append ( wx.ID_ANY, 'Font' )
        self.Bind ( wx.EVT_MENU, self.OnFont, f1 )

        viewMenu.AppendSeparator()

        f2 = viewMenu.Append ( wx.ID_ANY, 'Light theme' )
        self.Bind ( wx.EVT_MENU, self.OnLightTheme, f2 )

        f3 = viewMenu.Append ( wx.ID_ANY, 'Dark theme' )
        self.Bind ( wx.EVT_MENU, self.OnDarkTheme, f3 )

        helpMenu = wx.Menu()
        menubar.Append ( helpMenu, '&Help' )

        h1 = helpMenu.Append ( wx.ID_HELP, 'Help' )
        self.Bind ( wx.EVT_MENU, self.OnHelp, h1 )

        h3 = helpMenu.Append ( wx.ID_ANY, 'Report issue' )
        self.Bind ( wx.EVT_MENU, self.OnReport, h3 )

        helpMenu.AppendSeparator()
        
        h2 = helpMenu.Append ( wx.ID_ABOUT, 'About TakeNotes' )
        helpMenu.Bind ( wx.EVT_MENU, self.OnAboutBox, h2 )

        self.SetMenuBar ( menubar )
        
        self.Show()

        if len ( argv ) == 2:

            global pathname
            pathname = argv[1]

            if '.txt' in pathname:

                with open ( pathname, 'r' ) as f:
                
                    self.text_ctrl.WriteText ( f.read() )
                    self.text_ctrl.SetInsertionPoint ( 0 )

                self.statusbar.SetStatusText ( addpath ( self, pathname ) )

            else:

                dialog = wx.MessageDialog ( None, 'File format not supported! Only .txt files supported!', 'Exclamation',
                             wx.OK | wx.ICON_EXCLAMATION )

    def OnLightTheme ( self, event ):

        with open ( 'C:\TakeNotes\Files\Storage.txt', 'r+' ) as f:

            if f.read() == '0':
                pass

            else:

                deleteContent ( f )
                f.write ( '0' )

                self.text_ctrl.SetBackgroundColour ( wx.WHITE )
                self.text_ctrl.SetForegroundColour ( wx.BLACK )
                
            f.close()

    def OnDarkTheme ( self, event ):

        with open ( 'C:\TakeNotes\Files\Storage.txt', 'r+' ) as f:

            if f.read() == '1':
                pass

            else:

                deleteContent ( f )
                f.write ( '1' )
                
                self.text_ctrl.SetBackgroundColour ( wx.BLACK )
                self.text_ctrl.SetForegroundColour ( wx.WHITE )

            f.close()
    
    def OnForgot ( self, event ):

        from webbrowser import open as web

        web ( 'mailto:aadharshvenkat06@gmail.com?subject=Forgot Decrypt Pin&body=Describe your problem' )

    def OnEncrypt ( self, event ):

        if pathname != "":

            from time import sleep

            text = self.text_ctrl.GetValue()
            result, pin = ( encrypt ( text ) )
            
            self.text_ctrl.Clear()

            self.text_ctrl.WriteText ( str ( result ) )
            writing ( self, pathname )

            pin = str ( 'IMPORTANT Decryption pin: ' + pin )

            wx.MessageBox ( pin, 'Info', 
            wx.OK | wx.ICON_INFORMATION )

        else:

            dialog = wx.MessageDialog ( None, 'Please save this file or open saved file!', 'Exclamation',
            wx.OK | wx.ICON_EXCLAMATION )

            dialog.ShowModal()

    def OnDecrypt ( self, event ):

        dl = wx.TextEntryDialog ( self, 'Enter file pin:', 'Decrypt file' ) 
		
        if dl.ShowModal() == wx.ID_OK:
          
            pin = dl.GetValue()

        text = decrypt ( self.text_ctrl.GetValue(), pin )

        if text == None:

            dialog = wx.MessageDialog ( None, 'Invalid pin entered', 'Error',
            wx.OK | wx.ICON_ERROR )
            
            dialog.ShowModal()
            return

        self.text_ctrl.Clear()
        self.text_ctrl.WriteText ( text )
        self.OnSave ( self )
        
    def OnHowEncrypt ( self, event ):

        from os import startfile

        startfile ( 'C:\TakeNotes\Files\How we encrypt.txt' )
       
    def OnReport ( self, event ):

        from webbrowser import open as web

        web ( 'https://github.com/TheUNOGuy/TakeNotes/issues/1' )

    def OnFont ( self, event ):

        dlg = wx.FontDialog ( self,wx.FontData() ) 
		
        if dlg.ShowModal() == wx.ID_OK:
            
            data = dlg.GetFontData() 
            font = data.GetChosenFont() 
            self.text_ctrl.SetFont ( font )
			
        dlg.Destroy()
    
    def OnAboutBox ( self, event ):

        description = """        TakeNotes, a Text Editor created in 2021 and aims to excel
        as much as possible with python! TakeNotes is also opensouce on GitHub
        allowing anyone to contribute!
        """

        info = wx.adv.AboutDialogInfo()

        info.SetIcon ( wx.Icon ( 'C:\TakeNotes\Icon\Icon.png', wx.BITMAP_TYPE_PNG ) )
        info.SetName ( 'TakeNotes' )
        info.SetVersion ( 'v1.2' )
        info.SetDescription ( description )
        info.SetCopyright ( '(C) 2021 TheUNOGuy' )
        info.SetWebSite( 'https://github.com/TheUNOGuy/TakeNotes' )
        info.AddDeveloper ( 'TheUNOGuy - Registered name on GitHub' )

        wx.adv.AboutBox ( info )
                
    def OnHelp ( self, event ):

        from os import startfile

        startfile ( 'C:\TakeNotes\Files\Help.txt' )
        
    def onGetTime ( self, event ):

        now = datetime.now().now()
        today = datetime.today()

        now = str ( now.strftime ( "%H:%M:%S" ) )
        date = str ( today.strftime ( "%B %d, %Y" ) )

        s = now + " " + date

        self.text_ctrl.WriteText ( s )

    def OnOpen ( self, event ):
        
        with wx.FileDialog ( self, "Open TXT file", wildcard = "TXT files (*.txt)|*.txt",
                       style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST ) as fileDialog:
        
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return   
            
            global pathname

            self.text_ctrl.Clear()
            
            pathname = fileDialog.GetPath() 
            
            with open ( pathname, 'r' ) as f:
                
                self.text_ctrl.WriteText ( f.read().replace ( "'", "" ) )
                self.text_ctrl.SetInsertionPoint ( 0 )
            
            f.close()
            self.statusbar.SetStatusText ( addpath ( self, pathname ) )
                
    def OnSave ( self, event ):
        
        try:
            writing ( self, pathname )
        
        except:
            
            self.OnSaveAs ( self )
    
    def OnSaveAs ( self, event ):
        
        with wx.FileDialog ( self, "Save TXT file", wildcard = "TXT files (*.txt)|*.txt",
                       style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT ) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                
                return     
            
            global pathname

            pathname = fileDialog.GetPath()
            
            fi = open ( pathname, 'w' )
            fi.close()
            
            writing ( self, pathname )
        self.statusbar.SetStatusText ( addpath ( self, pathname ) )
    
    def OnNew ( self, event ):
            
        dial = wx.MessageDialog ( None, 'Do you want to save?', 'Question',
        wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION )
            
        choice = dial.ShowModal()
            
        if choice == wx.ID_YES:
            
            if pathname == '':
                
                self.OnSaveAs ( self )
                
            else:
                writing ( self, pathname )
            
        if choice == wx.ID_CANCEL:
            return
        
        self.text_ctrl.Clear()
        
        resetPath()
    
    def OnQuit ( self, event ):

        self.Close()
    
    def OnCut ( self, event ):
        
        hotkey ( 'ctrl', 'x' )
        
        hotkey ( 'ctrl', 'x' )
    
    def OnCopy ( self, event ):
        
        hotkey ( 'ctrl', 'c' )
    
    def OnPaste ( self, event ):
        
        hotkey ( 'ctrl', 'v' )
    
    def OnUndo ( self, event ):
        
        hotkey ( 'ctrl', 'z' )
    
    def OnSelectAll ( self, event ):
        
        hotkey ( 'ctrl', 'a' )   

    def OnDelete ( self, event ):
        
        hotkey ( 'delete' )
    
    def OnExit ( self, event ):
        
        if event.GetEventType() == wx.EVT_CLOSE.typeId:

            if pathname == "" and self.text_ctrl.GetValue() == "":
                pass

            else:
            
                dial = wx.MessageDialog ( None, 'Do you want to save?', 'Question',
                wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION )
            
                choice = dial.ShowModal()
            
                if choice == wx.ID_CANCEL:
                    return
            
                elif choice == wx.ID_YES:
        
                    try:
                    
                        writing ( self, pathname )
        
                    except:
            
                        self.OnSaveAs ( self )
                        return
            
            self.Destroy()

if __name__ == '__main__':
    
    
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
