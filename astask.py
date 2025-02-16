import sys
import os
import json
from astask_module import *

# main program


# Version : AS-TaskManager(v2025.02.16 Unstable)
# © 2025 Abyasa Saifaji <aby110605@gmail.com>


# to make sure only get 2nd arg and after that
args = sys.argv[1:]

# if bool(argv) -> checking if argv exist
if args:
    # put first arg into func
    func = args[0]
    
    if func == '-h':
        help()
    elif func == 'help':
        help()
    elif func == 'add':
        add(args)
    elif func == 'rm':
        if (args[1]) == "-db":
            deldb(args)
        else:
            delt(args)
    elif func == 'create':
        createdb(args)
    else:
        print(f"Argument invalid, {func} is not a valid argument")
        
else:
    welcome_ver()