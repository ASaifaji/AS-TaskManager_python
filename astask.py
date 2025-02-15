import sys
import json
from astask_module import *

# Version : AS-TaskManager(v2025.02.16 Unstable)
# © 2025 Abyasa Saifaji <aby110605@gmail.com>

# to make sure only get 2nd arg and after that
args = sys.argv[1:]

# if bool(argv) -> checking if argv exist
if args:
    func_name = args[0]
    if args[0] == '-h':
        help()
    elif args[0] == 'help':
        help()
    elif args[0] == '3':
        print()
    elif args[0] == '4':
        print()
    else:
        print(f"Argument invalid, {args[0]} is not a valid argument")
else:
    welcome_ver()