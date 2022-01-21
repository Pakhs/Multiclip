#!/usr/bin/env python3
import pyperclip
import json
import sys


#==================================
#Variables you can change
#==================================

#Name of the file that includes all your saved clipboards
#Unencrypted so don't save any passwords
FILENAME = 'clip.json' 

#==================================
#Do not change anything under this
#line if you do not know what you
#are doing
#==================================



#Basic json open and close file functions
def open_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return {}
def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

#data file opening
data = open_data(FILENAME)

#Color class and functions, just for printing purposes
class Colour:
    def __init__(self, c, next = None):
        self.error = "\033[1;31m"
        self.end = "\033[0m"
        self.c = c
        self.next = None

def addColors(colour1, colour2):
    colour1.next = colour2
    colour2.next = colour1
def getColour():
    colour1 = Colour("\033[1;34m")
    colour2 = Colour("\033[1;35m")
    addColors(colour1, colour2)
    colour = colour1
    while True:
        colour = colour.next
        yield colour


#Command functions
def save(key):
    data[key] = pyperclip.paste()
    save_data(FILENAME, data)
    for colour in getColour():
        break
    print(f"> Succesffully saved.\n> Key: {colour.c}{key}{colour.end}\n> Value: {colour.next.c}{pyperclip.paste()}{colour.end}")

def load(key):
    for colour in getColour():
        break
    try:
        pyperclip.copy(data[key])
    except:
        print(f'{colour.error}Error, key does not exist{colour.end}')
        exit(0)
    print(f"> Succesffully loaded.\n> Current clipboard: {colour.c}{data[key]}{colour.end}")

def print_list():
    for colour in getColour():
        break
    if data == {}:
        print(f'{colour.error}Error, no saved values{colour.end}')
        exit(0)
    print('=-=-=-=-=-=-=-=-=-=')
    for key in data.keys():
        print(f'{colour.c}{key}:\n{data[key]}{colour.end}\n=-=-=-=-=-=-=-=-=-=')
        colour = colour.next

def remove_key(key):
    for colour in getColour():
        break
    if key in data:
        data.pop(key)
        print(f"Successfully removed {colour.c}{key}{colour.end} from file")
        save_data(FILENAME, data)
    else:
        print(f'{colour.error}Error, key not found{colour.end}')



#Command handler based on the arguments of the programme
def commandHandler():
    for colour in getColour():
        break
    command_len = len(sys.argv)
    if command_len != 2 and command_len != 3:
        print(f'{colour.error}Incorrect ammount of arguments!{colour.end}')
        exit(0)
    command = sys.argv[1]
    if command == '-s':
        if command_len != 3:
            print(f"{colour.error}Error, correct usage:\n./{sys.argv[0]} -s [key]{colour.end}")
            exit(0)
        save(sys.argv[2])
    elif command == '-l':
        if command_len != 3:
            print(f"{colour.error}Error, correct usage:\n./{sys.argv[0]} -l [key]{colour.end}")
            exit(0)
        load(sys.argv[2])
    elif command == '-p':
        if command_len != 2:
            print(f"{colour.error}Error, correct usage:\n./{sys.argv[0]} -p{colour.end}")
            exit(0)
        print_list()
    elif command == '-r':
        if command_len != 3:
            print(f"{colour.error}Error, correct usage:\n./{sys.argv[0]} -r [key]{colour.end}")
            exit(0)
        remove_key(sys.argv[2])
    else:
        print(f"{colour.error}Unknown command{colour.end}")
        
#main function of the programme
def main():
    commandHandler()

#Running the main function of the script
if __name__ == '__main__':
    main()

