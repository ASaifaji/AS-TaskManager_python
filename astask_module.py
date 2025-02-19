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
    print()
    print("ASTask  Copyright (C) 2025  Abyasa Saifaji")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions.")
    print("")
    print("Type \"python astask.py -h\" or \"python astask.py help\" for help")
    print("")

def createdb(args):
    
    db = {"task":[]}
    
    if len(args) == 1:
        dbname = str(input("New Database Name: "))
    else:
        dbname = args[1]

    if dbname[0] != "-":
        with open(f"{dbname}.json", "w") as f:
            json.dump(db, f, indent=4)
    else:
        print("dbname can't start with \"-\"")

def add(args):
    dbname =args[1]
    db = load(dbname)
    if db != None:
        task_name = ' '.join(args[2:])
        if db["task"] == []:
            db["task"].append({"id":1,"task_name":f"{task_name}","status":"to-do"})
        else:
            db["task"].append({"id":len(db["task"])+1,"task_name":f"{task_name}","status":"to-do"})
        
        save(dbname, db)

def load(dbname):
    try :
        with open(f"{dbname}.json") as f:
            db = json.load(f)
            return db
    except FileNotFoundError:
        print(f"{dbname} doesn't exist in directory")

def save(dbname, db):
    try :
        with open(f"{dbname}.json", "w") as f:
            json.dump(db, f, indent=4)
    except FileNotFoundError:
        print(f"can't save, {dbname} doesn't exist in directory")

def delt(args):
    task_name = ' '.join(args[2:])
    dbname =args[1]
    db = load(dbname)
    
    for x in db["task"]:
        if x["task_name"] == task_name:
            index = x["id"]-1
            break
    
    for x in db["task"]:
        if x["id"] >= index+2:
            x["id"] -= 1
    
    if index == 0:
        db["task"] = db["task"][1:]
    elif index == len(db["task"])-1:
        db["task"] = db["task"][:-1]
    else:
        db["task"] = db["task"][:index] + db["task"][index+1:]
    
    save(dbname, db)
    

def deldb(args):
    if len(args) == 2:
        path = str(input("db name : ")) + ".json"
    else:
        path = f"{args[2]}.json"
    os.remove(path)