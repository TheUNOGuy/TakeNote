
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
from dataclasses import dataclass
import threading
from keyboard import is_pressed
from time import sleep
from re import escape
from ast import literal_eval
from webbrowser import open as web

@dataclass
class storage:

    pathname: str

store = storage ( "" )

saveText = ''
wrap = ''

def wordWrapCheck():

    with open ( 'C:\TakeNotes\Files\Storage.txt', 'r+' ) as f:

        l = f.read()
        l = list ( literal_eval ( l ) )

        if l[1] == '1':
            return 1

        if l[1] == '0':
            return 0
    f.close()

def fileName ( path ):

    from os.path import split as slicing

    h, file = slicing ( path )
    return file + " - TakeNotes"


def checkDarkTheme ( self ):

    with open ( 'C:\TakeNotes\Files\Storage.txt', 'r' ) as theme:

        checkTheme = theme.read()
        checkTheme = list ( literal_eval ( checkTheme ) )

        if checkTheme[0] == '1':

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

    global store
    
    store = storage ( "" )

def deleteContent ( file ):

    file.seek ( 0 )
    file.truncate()
    file.seek ( 0 ) 

    return file

class MyFrame ( wx.Frame ):
    
    def __init__( self ):
        
        super().__init__ ( parent = None, title = 'TakeNotes', size = ( 800, 500 ) )
        panel = wx.Panel ( self )

        self.SetIcon ( wx.Icon ( "C:\TakeNotes\Icon\Icon.png" ) )
        
        sizer = wx.BoxSizer ( wx.VERTICAL )
        n = wordWrapCheck()
        if n == 1:
            self.text_ctrl = wx.TextCtrl ( panel, pos = ( 0, 0 ), style = wx.TE_MULTILINE | wx.TE_CHARWRAP | wx.TE_RICH | wx.BORDER_NONE )
        if n == 0:
            self.text_ctrl = wx.TextCtrl ( panel, pos = ( 0, 0 ), style = wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_RICH | wx.BORDER_NONE )
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
        
        m0 = fileMenu.Append ( wx.ID_NEW, 'New\tCtrl+N' )
        self.Bind ( wx.EVT_MENU, self.OnNew, m0 )
        
        fileMenu.AppendSeparator()
        
        m1 = fileMenu.Append ( wx.ID_SAVE, 'Save\tCtrl+S' )
        self.Bind ( wx.EVT_MENU, self.OnSave, m1 )
        
        m4 = fileMenu.Append ( wx.ID_SAVEAS, 'Save as...' )
        self.Bind ( wx.EVT_MENU, self.OnSaveAs, m4 )
        
        m3 = fileMenu.Append ( wx.ID_OPEN, 'Open...\tCtrl+O' )
        self.Bind ( wx.EVT_MENU, self.OnOpen, m3 )

        fileMenu.AppendSeparator()

        m5 = fileMenu.Append ( wx.ID_ANY, 'Convert to PDF\tCtrl+P' )
        self.Bind ( wx.EVT_MENU, self.OnPDF, m5 )
        
        fileMenu.AppendSeparator()
        
        m2 = fileMenu.Append ( wx.ID_EXIT, 'Force Quit' )
        self.Bind ( wx.EVT_MENU, self.OnQuit, m2 )
        self.Bind ( wx.EVT_CLOSE, self.OnExit )
        
        editMenu = wx.Menu()
        menubar.Append ( editMenu, '&Edit' )
        
        c1 = editMenu.Append ( wx.ID_CUT, 'Cut\tCtrl+X' )
        self.Bind ( wx.EVT_MENU, self.OnCut, c1 )
        
        c2 = editMenu.Append ( wx.ID_COPY, 'Copy\tCtrl+C' )
        self.Bind ( wx.EVT_MENU, self.OnCopy, c2 )
        
        c3 = editMenu.Append ( wx.ID_PASTE, 'Paste\tCtrl+V' )
        self.Bind ( wx.EVT_MENU, self.OnPaste, c3 )
        
        editMenu.AppendSeparator()
        
        e1 = editMenu.Append ( wx.ID_UNDO, 'Undo\tCtrl+Z' )
        self.Bind ( wx.EVT_MENU, self.OnUndo, e1 )
        
        e3 = editMenu.Append ( wx.ID_DELETE, 'Delete\tDel' )
        self.Bind ( wx.EVT_MENU, self.OnDelete, e3 )
        
        e2 = editMenu.Append ( wx.ID_SELECTALL, 'Select All\tCtrl+A' )
        self.Bind ( wx.EVT_MENU, self.OnSelectAll, e2 )

        editMenu.AppendSeparator()

        rep = editMenu.Append ( wx.ID_REPLACE, 'Replace...\tCtrl+H' )
        self.Bind ( wx.EVT_MENU, self.OnReplace, rep )

        e4 = editMenu.Append ( wx.ID_ANY, 'Insert Date/Time\tF5' )
        self.Bind ( wx.EVT_MENU, self.onGetTime, e4 )

        enMenu = wx.Menu()
        menubar.Append ( enMenu, 'Encryption' )

        en1 = enMenu.Append ( wx.ID_ANY, 'Encryption Info' )
        self.Bind ( wx.EVT_MENU, self.OnHowEncrypt, en1 )

        enMenu.AppendSeparator()

        en2 = enMenu.Append ( wx.ID_ANY, 'Encrypt file\tCtrl+E' )
        self.Bind ( wx.EVT_MENU, self.OnEncrypt, en2 )

        en3 = enMenu.Append ( wx.ID_ANY, 'Decrypt file\tCtrl+D' )
        self.Bind ( wx.EVT_MENU, self.OnDecrypt, en3 )

        enMenu.AppendSeparator()

        en4 = enMenu.Append ( wx.ID_ANY, 'Forgot Pin' )
        self.Bind ( wx.EVT_MENU, self.OnForgot, en4 )

        viewMenu = wx.Menu()
        menubar.Append ( viewMenu, '&View' )

        f1 = viewMenu.Append ( wx.ID_ANY, 'Font' )
        self.Bind ( wx.EVT_MENU, self.OnFont, f1 )

        f4 = viewMenu.Append ( wx.ID_ANY, 'Word wrap...', kind = wx.ITEM_CHECK )
        self.Bind ( wx.EVT_MENU, self.OnWrap, f4 )
        if n == 1:
            f4.Check()

        viewMenu.AppendSeparator()

        f3 = viewMenu.Append ( wx.ID_ANY, 'Dark theme\tCtrl+T', kind = wx.ITEM_CHECK )
        self.Bind ( wx.EVT_MENU, self.OnTheme, f3 )
        
        with open ( 'C:\TakeNotes\Files\Storage.txt', 'r' ) as theme:

            checkTheme = theme.read()
            checkTheme = list ( literal_eval ( checkTheme ) )

            if checkTheme[0] == '1':
                f3.Check()

            theme.close()

        helpMenu = wx.Menu()
        menubar.Append ( helpMenu, '&Help' )

        h1 = helpMenu.Append ( wx.ID_HELP, 'Help\tF1' )
        self.Bind ( wx.EVT_MENU, self.OnHelp, h1 )

        helpMenu.AppendSeparator()

        h3 = helpMenu.Append ( wx.ID_ANY, 'Report issue' )
        self.Bind ( wx.EVT_MENU, self.OnReport, h3 )

        h4 = helpMenu.Append ( wx.ID_ANY, 'TakeNotes Forum' )
        self.Bind ( wx.EVT_MENU, self.OnForum, h4 )

        h5 = helpMenu.Append ( wx.ID_ANY, 'Send Feedback' )
        self.Bind ( wx.EVT_MENU, self.OnFeedback, h5 )

        helpMenu.AppendSeparator()
        
        h2 = helpMenu.Append ( wx.ID_ABOUT, 'About TakeNotes' )
        helpMenu.Bind ( wx.EVT_MENU, self.OnAboutBox, h2 )

        self.SetMenuBar ( menubar )
        
        self.Show()

        if len ( argv ) == 2:

            global store
            store = storage ( argv[1] )

            if '.txt' in store.pathname:

                with open ( store.pathname, 'r' ) as f:
                
                    self.text_ctrl.WriteText ( f.read() )
                    self.text_ctrl.SetInsertionPoint ( 0 )

                    self.SetTitle ( fileName ( store.pathname ) )
                    f.close()

                self.statusbar.SetStatusText ( addpath ( self, store.pathname ) )

            else:

                dialog = wx.MessageDialog ( None, 'File format not supported! Only .txt files supported!', 'Exclamation',
                             wx.OK | wx.ICON_EXCLAMATION )

                dialog.ShowModal()

    def OnPDF ( self, event ):

        from fpdf import FPDF

        global store
            
        pdf = FPDF()   
        pdf.add_page()
        
        if store.pathname != "":
            file = open ( store.pathname, 'r' )

        else:
            dialog = wx.MessageDialog ( None, 'Please open a saved file or save this file!', 'Exclamation',
                             wx.OK | wx.ICON_EXCLAMATION )

            dialog.ShowModal()
            return

        di = wx.TextEntryDialog ( self, 'Title for the PDF file ( Type * if you don\'t want a title )', 'Title' )

        if di.ShowModal() == wx.ID_OK:
            title = str ( di.GetValue() )

        if title != '*':
            pdf.set_font ( "Arial", 'B', size = 10 )
            pdf.cell ( 200, 10, txt = title, ln = 1, align = 'A' )
            
        pdf.set_font ( "Arial", size = 10 )

        with wx.FileDialog ( self, "Save PDF file", wildcard = "PDF files (*.pdf)|*.pdf",
                       style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT ) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            output = fileDialog.GetPath()

        for i in file:
            pdf.cell ( 200, 10, txt = i, ln = 2, align = 'A' )
            
        pdf.output ( output )
        from os import startfile
        startfile ( output )

    def OnReplace ( self, event ):

        import re
        
        d = wx.TextEntryDialog ( self, 'What should be replaced in the document?', 'Replace' ) 
		
        if d.ShowModal() == wx.ID_OK:

            rep = d.GetValue()
          
            d2 = wx.TextEntryDialog ( self, '"{}" should be replaced by?'.format ( rep ), 'Replace' )

            if d2.ShowModal() == wx.ID_OK:

                rep2 = d2.GetValue()

        text = re.compile ( re.escape ( rep ), re.IGNORECASE ) 
        text = text.sub ( rep2, self.text_ctrl.GetValue() ) 
        print ( text )
        self.text_ctrl.Clear()
        self.text_ctrl.WriteText ( str ( text ) )

    def OnWrap ( self, event ):

        with open ( 'C:\TakeNotes\Files\Storage.txt', 'r+' ) as f:

            l = f.read()
            l = list ( literal_eval ( l ) )

            if l[1] == '1':

                wx.MessageBox ( 'Please restart TakeNotes for the changes to apply', 'Info', 
                wx.OK | wx.ICON_INFORMATION )
                l[1] = '0'

            elif l[1] == '0':

                wx.MessageBox ( 'Please restart TakeNotes for the changes to apply', 'Info', 
                wx.OK | wx.ICON_INFORMATION )
                l[1] = '1'
        
            deleteContent ( f )
            f.write ( str ( l ) )

        f.close()

    def OnForum ( self, event ):

        web ( 'https://github.com/TheUNOGuy/TakeNotes/discussions' )

    def OnFeedback ( self, event ):

        web ( 'https://github.com/TheUNOGuy/TakeNotes/discussions/5' )

    def OnTheme ( self, event ):

        with open ( 'C:\TakeNotes\Files\Storage.txt', 'r+' ) as f:

            l = f.read()
            l = list ( literal_eval ( l ) )
            l[0] = str ( l[0] )

            if l[0] == '1':
                
                self.text_ctrl.SetBackgroundColour ( wx.WHITE )
                self.text_ctrl.SetForegroundColour ( wx.BLACK )
                l[0] = '0'

            else:

                self.text_ctrl.SetBackgroundColour ( wx.BLACK )
                self.text_ctrl.SetForegroundColour ( wx.WHITE )
                l[0] = '1'

            deleteContent ( f )
            f.write ( str ( l ) )

        f.close()

    def OnForgot ( self, event ):

        web ( 'mailto:aadharshvenkat06@gmail.com?subject=Forgot Decrypt Pin&body=Describe your problem' )

    def OnEncrypt ( self, event ):

        dialog = wx.MessageDialog ( None, 'This will encrypt your file and give a decyption pin. Do you want to continue?', 'Exclamation',
        wx.YES_NO | wx.ICON_EXCLAMATION )

        c = dialog.ShowModal()

        if c == wx.ID_YES:
            pass

        else:
            return

        if store.pathname != "":

            from time import sleep

            text = self.text_ctrl.GetValue()
            result, pin = ( encrypt ( text ) )
            
            self.text_ctrl.Clear()

            self.text_ctrl.WriteText ( str ( result ) )
            writing ( self, store.pathname )

            pin = str ( 'IMPORTANT! Decryption pin: ' + pin )

            wx.MessageBox ( pin, 'Info', 
            wx.OK | wx.ICON_INFORMATION )

            global saveText
            saveText = self.text_ctrl.GetValue()

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

        web ( 'https://github.com/TheUNOGuy/TakeNotes/issues/3' )

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
        info.SetVersion ( 'v1.3' )
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

        global store
        
        with wx.FileDialog ( self, "Open TXT file", wildcard = "TXT files (*.txt)|*.txt",
                       style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST ) as fileDialog:
        
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.text_ctrl.Clear()

            store = storage ( fileDialog.GetPath() )
            
            with open ( store.pathname, 'r' ) as f:
                
                self.text_ctrl.WriteText ( f.read().replace ( "'", "" ) )
                self.text_ctrl.SetInsertionPoint ( 0 )
                self.SetTitle ( fileName ( store.pathname ) )
                global saveText
                saveText = self.text_ctrl.GetValue()
            
            f.close()
            self.statusbar.SetStatusText ( addpath ( self, store.pathname ) )
                
    def OnSave ( self, event ):

        global store
        
        try:
            writing ( self, store.pathname )

            global saveText
            saveText = self.text_ctrl.GetValue()
        
        except:
            
            self.OnSaveAs ( self )
    
    def OnSaveAs ( self, event ):

        global store
        
        with wx.FileDialog ( self, "Save TXT file", wildcard = "TXT files (*.txt)|*.txt",
                       style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT ) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                
                return
            
            store = storage ( fileDialog.GetPath() )
            
            fi = open ( store.pathname, 'w' )
            fi.close()
            
            writing ( self, store.pathname )
            
        self.statusbar.SetStatusText ( addpath ( self, store.pathname ) )
        self.SetTitle ( fileName ( store.pathname ) )
        global saveText
        saveText = self.text_ctrl.GetValue()
        
    def OnNew ( self, event ):

        global store
        
        global saveText
        if saveText != self.text_ctrl.GetValue():
            
            dial = wx.MessageDialog ( None, 'Do you want to save?', 'Question',
            wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION )
            
            choice = dial.ShowModal()
            
            if choice == wx.ID_YES:
            
                if store.pathname == '':
                    self.OnSaveAs ( self )
                
                else:
                    writing ( self, store.pathname )
            
            if choice == wx.ID_CANCEL:
                return
        
        self.text_ctrl.Clear()
        self.statusbar.SetStatusText ( "" )
        resetPath()

    def OnQuit ( self, event ):
        self.Close()
    
    def OnCut ( self, event ):
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
            
            global saveText
            if saveText == self.text_ctrl.GetValue():
                pass

            else:
            
                dial = wx.MessageDialog ( None, 'Do you want to save?', 'Question',
                wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION )
            
                choice = dial.ShowModal()
            
                if choice == wx.ID_CANCEL:
                    return
            
                elif choice == wx.ID_YES:
        
                    try:
                        writing ( self, store.pathname )
        
                    except:
                        self.OnSaveAs ( self )
                        return
            
            self.Destroy()

if __name__ == '__main__':
    
    
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
