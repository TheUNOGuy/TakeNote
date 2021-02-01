
import random
import string
from os.path import join as jon
from pathlib import Path        
from ast import literal_eval
from re import escape

an = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

def make_file ( path ):

    with open ( path, 'w' ) as f:
        f.close()

def encrypt ( text ):

    result = ""
    private_key = []

    for i in text:

        if i in an:

            rand = random.randint ( 1, 5 )
            en = rand + ord ( i )
            en = chr ( en )
            en = str ( en )

            private_key.append ( rand )

            result = result + en

        else:
            result = result + str ( i )
            private_key.append ( " " )

    h = str ( Path.home() )

    path = jon ( h, 'AppData\Local\TN' )

    r = ''.join ( random.choice ( string.ascii_uppercase + string.digits ) for _ in range ( 5 ) )
    pin = r
    
    r = r + '.txt'

    path = jon ( path, r )
    make_file ( path )

    with open ( path, 'r+' ) as f:

        f.write ( str ( private_key ) )
        f.close()
    
    return result, pin

def decrypt ( result, pin ):

    h = str ( Path.home() )

    path = jon ( h, 'AppData\Local\TN' )
    pin = str ( pin + ".txt" )

    path = jon ( path, pin )

    try:

        from os import remove
        
        with open ( path, 'r' ) as f:

            private_key = list ( literal_eval ( f.read() ) )
            f.close()

        remove ( path )

    except:
        return

    counter = 0
    text = ""

    for i in result:

        if private_key [ counter ] != " ":
            
            char = i

            char = int ( ord ( char ) )
            char = char - private_key [ counter ]
            char = str ( chr ( char ) )

            text = text + char

        else:
            text = text + str ( i )

        counter = counter + 1

    return text

def getFileName ( path ):

    path = escape ( path )
    path = path.replace ( "\\", "//" )
    path = path[::-1]
    file = ""
    counter = 0
    checking = 0

    for i in range ( len ( path ) ):

        check = str ( path[counter] + path[counter+1] )

        if check == "//":
            if checking == 2:
                file = file.replace ( "/", "" )
                return file[::-1]
            checking = checking + 1

        else:
            file = file + path[counter]

        counter = counter + 1
