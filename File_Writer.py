from os import system, name, path
from FileHandler import FileHandler
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
        
def quit():
    FH.save()
    clear()
    exit()
    
def ask(msg, err = "", valid = 0, clr = True):
    if clr: clear()
    out = input("{}\n\n{}: ".format("" if not bool(valid) else err if not callable(err) else err(), msg))
    if out.lower() == "quit": quit() 
    else: return out

clear()
print("You may type \"quit\" at any input to write existing data to file and exit.\nIf you don't quit this way, your file isn't getting written so do it right!\n")
file = ask("Enter file path and name")
FH = FileHandler(file)

while True:
    clear()
    valid = 0
    while not bool(valid%2):
        type = ask("Select variable type\n1. String\n2. Int\3. Float\4. File\n[]", "Invalid Selection!", valid)
        valid += int(type in ["1", "2", "3", "4", "quit"]) + 2
        
    valid = 0
    if type == "1":
        to_write = ask("Enter string")
    elif type == "2":
        while not bool(valid%2):
            to_write = ask("Enter integer", "That's not an integer.", valid)
            try:
                int(to_write)
                valid = 1
            except:
                valid = 2
    elif type == "3":
        while not bool(valid%2):
            to_write = ask("Enter floating point number", "That's not a floating point number", valid)
            try:
                float(to_write)
                valid = 1
            except:
                valid = 2
    elif type == "4":
        while not bool(valid%2):
            cont = ask("The contents of a file must be added last. If you continue, this file will automatically be saved and the script will close.\nContinue? (y)es/(n)o", "That was a yes or no question", valid)
            if cont not in ["y", "yes", "n", "no"]:
                valid = 2
            else:
                valid = 0
                while not bool(valid%2):
                    clear()
                    Tk().withdraw()
                    f_path = askopenfilename()
                    if not path.exists(f_path):
                        valid = 2
                    else:
                        FH.write(open(f_path, "rb").read())
                        valid = 1
        quit()
    else:
        quit()
        
    FH.write(to_write)
