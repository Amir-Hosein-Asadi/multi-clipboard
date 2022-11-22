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

#if len(sys.argv) == 2:
#    command = sys.argv[1]
#    print(command)

def save_items(filepath, data):
    with open(filepath , 'w') as f:
        json.dump(data, f)
        
save_items("test.json", {"key": "value"})

def load_items(filepath):
    with open(filepath , 'r') as f:
        data = json.load(f)
        return data

if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == "save":
        print(command)
    elif command == "load":
        print(command)
    elif command == "list":
        print(command)
    else:
        print("Unknown command")

else:
    print("Please write exactly one command.")