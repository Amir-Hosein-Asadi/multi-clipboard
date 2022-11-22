import sys 
import clipboard
import json

#data = clipboard.paste()
#print(data)
#-----------------------------------------------------------------------------
#clipboard.copy("abs")
#-----------------------------------------------------------------------------
#run this python script directly from command line
#-----------------------------------------------------------------------------
#print(sys.argv[1:])
#print(sys.argv)
#-----------------------------------------------------------------------------
#if statement that checks exactly one command

if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)
