
'''
Files have been filed under an MIT license.

Made by the TheUNOGuy ( Registered name in GitHub )

Free to contribute,
Pull requests can be given by anyone!
'''

import wx
import wx.adv
from sys import argv
from pyautogui import hotkey
from datetime import datetime

pathname = ''

def addpath ( self, path ):

    return "File: " + path

def writing ( self, path ):
    
    text = self.text_ctrl.GetValue()
    
    with open ( path, 'r+' ) as f:
        
        deleteContent ( f )
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
        self.text_ctrl = wx.TextCtrl ( panel, pos = ( 1, 1 ), style = wx.TE_MULTILINE | wx.HSCROLL )
        sizer.Add ( self.text_ctrl, 1, wx.ALL | wx.EXPAND, 1 )

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

        fontMenu = wx.Menu()
        menubar.Append ( fontMenu, '&Font' )

        f1 = fontMenu.Append ( wx.ID_ANY, 'Font' )
        self.Bind ( wx.EVT_MENU, self.OnFont, f1 )

        helpMenu = wx.Menu()
        menubar.Append ( helpMenu, '&Help' )

        h1 = helpMenu.Append ( wx.ID_HELP, 'Help' )
        self.Bind ( wx.EVT_MENU, self.OnHelp, h1 )

        h3 = helpMenu.Append ( wx.ID_ANY, 'Report issue' )
        self.Bind ( wx.EVT_MENU, self.OnReport, h3 )

        helpMenu.AppendSeparator()

        h2 = helpMenu.Append ( wx.ID_ANY, 'About TakeNotes' )
        helpMenu.Bind ( wx.EVT_MENU, self.OnAboutBox, h2 )

        self.SetMenuBar ( menubar )
        
        self.Show()

        if len ( argv ) == 2:

            global pathname
            pathname = argv[1]

            if '.txt' in pathname:

                with open ( pathname, 'r' ) as f:
                
                    self.text_ctrl.WriteText ( f.read() )

                self.statusbar.SetStatusText ( addpath ( self, pathname ) )

            else:

                dialog = wx.MessageDialog ( None, 'File format not supported! Only .txt files supported!', 'Exclamation',
                             wx.OK | wx.ICON_EXCLAMATION )

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
        info.SetVersion ( 'v1.1' )
        info.SetDescription ( description )
        info.SetCopyright ( '(C) 2021 TheUNOGuy' )
        info.SetWebSite( 'https://github.com/TheUNOGuy/TakeNotes' )
        info.AddDeveloper ( 'TheUNOGuy - Registered name on GitHub' )

        wx.adv.AboutBox ( info )
                
    def OnHelp ( self, event ):

        from os import startfile

        startfile ( 'C:\TakeNotes\Help.txt' )
        
    def onGetTime ( self, event ):

        now = datetime.now().now()
        today = datetime.today()

        now = str ( now.strftime ( "%H:%M:%S" ) )
        date = str ( today.strftime ( "%B %d, %Y" ) )

        s = now + " " + date

        self.text_ctrl.WriteText ( s )

    def OnOpen ( self, event ):
        
        with wx.FileDialog ( self, "Open TXT file", wildcard="TXT files (*.txt)|*.txt",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
        
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return   
            
            global pathname
            
            pathname = fileDialog.GetPath() 
            
            with open ( pathname, 'r' ) as f:
                
                self.text_ctrl.WriteText ( f.read() )
            
            f.close()
            self.statusbar.SetStatusText ( addpath ( self, pathname ) )
                
    def OnSave ( self, event ):
        
        try:
            writing ( self, pathname )
        
        except NameError:
            
            dial = wx.MessageDialog ( None, 'Please \'Save as\' first!', 'Exclamation',
            wx.OK | wx.ICON_EXCLAMATION )
            
            dial.ShowModal()
    
    def OnSaveAs ( self, event ):
        
        with wx.FileDialog ( self, "Save TXT file", wildcard = "TXT files (*.txt)|*.txt",
                       style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

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
                
                dialog = wx.MessageDialog ( None, 'Please \'Save as\' first!', 'Exclamation',
                             wx.OK | wx.ICON_EXCLAMATION )
            
                dialog.ShowModal()
                
            else:
                writing ( self, pathname )
            
        if choice == wx.ID_CANCEL:
            return
        
        hotkey ( 'ctrl', 'a' )
        hotkey ( 'delete' )
        
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
    
    def OnExit(self, event):
        
        if event.GetEventType() == wx.EVT_CLOSE.typeId:
            
            dial = wx.MessageDialog ( None, 'Do you want to save?', 'Question',
            wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION )
            
            choice = dial.ShowModal()
            
            if choice == wx.ID_CANCEL:
                return
            
            elif choice == wx.ID_YES:
        
                try:
                    
                    writing ( self, pathname )
        
                except:
            
                    dialog = wx.MessageDialog ( None, 'Please \'Save as\' first!', 'Exclamation',
                             wx.OK | wx.ICON_EXCLAMATION )
            
                    dialog.ShowModal()
                    return
            
            self.Destroy()

if __name__ == '__main__':
    
    
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
