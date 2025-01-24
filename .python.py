#!/usr/bin/python3

import sys
if len(sys.argv) != 2:
    print("Usage: python3 python.py <name>")
    sys.exit(1)

# Get the victim's name from the command-line argument
name = sys.argv[1]



# ______   _______ _   _  ___  _   _
#|  _ \ \ / /_   _| | | |/ _ \| \ | |
#| |_) \ V /  | | | |_| | | | |  \| |
#|  __/ | |   | | |  _  | |_| | |\  |
#|_|    |_|   |_| |_| |_|\___/|_| \_|
# _   _    _    ____ _  _____ _   _  ____
#| | | |  / \  / ___| |/ /_ _| \ | |/ ___|
#| |_| | / _ \| |   | ' / | ||  \| | |  _
#|  _  |/ ___ \ |___| . \ | || |\  | |_| |
#|_| |_/_/   \_\____|_|\_\___|_| \_|\____|



#Phase 1
for i in range(1, 1001):
    print(name + str(i))
for i in range(1, 1001):
    print(name + str(i) + "@")
for i in range(1, 1001):
    print(name + str(i) + "#")
for i in range(1, 1001):
    print(name + str(i) + "@#")
for i in range(1, 1001):
    print(name + str(i) + "#@")

#Phase 2
for i in range(1, 1001):
    print(name.capitalize() + str(i))
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "@")
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "#")
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "@#")
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "#@")

#Phase 3
for i in range(1, 1001):
    print(str(i) + name)
for i in range(1, 1001):
    print(str(i) + name + "@")
for i in range(1, 1001):
    print(str(i) + name + "#")
for i in range(1, 1001):
    print(str(i) + name + "@#")
for i in range(1, 1001):
    print(str(i) + name + "#@")

#Phase 4
for i in range(1, 1001):
    print(name.capitalize() + str(i))
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "@")
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "#")
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "@#")
for i in range(1, 1001):
    print(name.capitalize() + str(i) + "#@")

#Phase 5
for i in range(1, 1001):
    print(name.upper() + str(i))
for i in range(1, 1001):
    print(name.upper() + str(i) + "@")
for i in range(1, 1001):
    print(name.upper() + str(i) + "#")
for i in range(1, 1001):
    print(name.upper() + str(i) + "@#")
for i in range(1, 1001):
    print(name.upper() + str(i) + "#@")

#Phase 6
for i in range(1, 1001):
    print(name.upper() + str(i))
for i in range(1, 1001):
    print(name.upper() + str(i) + "@")
for i in range(1, 1001):
    print(name.upper() + str(i) + "#")
for i in range(1, 1001):
    print(name.upper() + str(i) + "@#")
for i in range(1, 1001):
    print(name.upper() + str(i) + "#@")

############################################
upname = name.replace("h", "7")
upname = name.replace("kh", "5")
upname = name.replace("t", "6")
upname = name.replace("s", "9")
upname = name.replace("a", "2")
############################################

#Phase 1
for i in range(1, 1001):
    print(upname + str(i))
for i in range(1, 1001):
    print(upname + str(i) + "@")
for i in range(1, 1001):
    print(upname + str(i) + "#")
for i in range(1, 1001):
    print(upname + str(i) + "@#")
for i in range(1, 1001):
    print(upname + str(i) + "#@")

#Phase 2
for i in range(1, 1001):
    print(upname.capitalize() + str(i))
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "@")
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "#")
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "@#")
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "#@")

# Phase 3
for i in range(1, 1001):
    print(str(i) + upname)
for i in range(1, 1001):
    print(str(i) + upname + "@")
for i in range(1, 1001):
    print(str(i) + upname + "#")
for i in range(1, 1001):
    print(str(i) + upname + "@#")
for i in range(1, 1001):
    print(str(i) + upname + "#@")

# Phase 4
for i in range(1, 1001):
    print(upname.capitalize() + str(i))
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "@")
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "#")
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "@#")
for i in range(1, 1001):
    print(upname.capitalize() + str(i) + "#@")

# Phase 5
for i in range(1, 1001):
    print(upname.upper() + str(i))
for i in range(1, 1001):
    print(upname.upper() + str(i) + "@")
for i in range(1, 1001):
    print(upname.upper() + str(i) + "#")
for i in range(1, 1001):
    print(upname.upper() + str(i) + "@#")
for i in range(1, 1001):
    print(upname.upper() + str(i) + "#@")

# Phase 6
for i in range(1, 1001):
    print(upname.upper() + str(i))
for i in range(1, 1001):
    print(upname.upper() + str(i) + "@")
for i in range(1, 1001):
    print(upname.upper() + str(i) + "#")
for i in range(1, 1001):
    print(upname.upper() + str(i) + "@#")
