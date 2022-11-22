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
SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath , 'w') as f:
        json.dump(data, f)
        
save_data("test.json", {"key": "value"})

def load_data(filepath):
    try:
        with open(filepath , 'r') as f:
            data = json.load(f)
            return data
    except:
        return{}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved!")
        
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Data not exist!")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")

else:
    print("Please write exactly one command.")