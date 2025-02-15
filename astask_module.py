# Version : AS-TaskManager(v2025.02.16 Unstable)
# © 2025 Abyasa Saifaji <aby110605@gmail.com>


def help():
    print("List of all AS-TaskManager command")
    print("add          add \"{your task}\"")
    print("update       ")
    print("delete       delete \"{your task}")
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