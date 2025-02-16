import json
import os

# module for astask.py

# Version : AS-TaskManager(v2025.02.16 Unstable)
# © 2025 Abyasa Saifaji <aby110605@gmail.com>


def help():
    print("List of all AS-TaskManager command")
    print("add          add a todo task to one of your db   ; add {dbname} {task}")
    print("update       ")
    print("rm           delete specified task from your db  ; rm {dbname} {task}")
    print("     -db     delete specified db                 ; rm -db {dbname}")
    print("ls           list all task")
    print("     -d      list all done task")
    print("     -n      list all not done task")
    print("     -p      list all on progress task")

def welcome_ver():
    print("\n")
    print("Welcome to AS-TaskManager.")
    print("Version : AS-TaskManager(v2025.02.16 Unstable)")
    print("\n")
    print("Type \"python astask.py -h\" or \"python astask.py help\" for help")
    print("\n")

def createdb(args):
    db = {"task":[]}
    print("\n")
    if len(args) == 1:
        # I might restrict naming later so it dont start with -, to avoid mistaking flag and file in other args
        dbname = str(input("New Database Name: "))
    else:
        dbname = args[1]
    with open(f"{dbname}.json", "w") as f:
        json.dump(db, f, indent=4)

def deldb(args):
    if len(args) == 2:
        path = str(input("db name : ")) + ".json"
    else:
        path = f"{args[2]}.json"
    os.remove(path)