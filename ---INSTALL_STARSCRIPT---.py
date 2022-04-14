#
#
#       Install StarScript!!
#           #NotDefected
#
#

import os
import shutil

Success = "\033[92m"
Error = "\033[91m"
Warning = "\033[93m"
Extra = "\033[95m"
Notice = "\033[94m"
Debug = "\033[90m"
Clear = "\033[0m"

print(f"{Clear}Welcome to the StarScript installer!")

print("Few Questions:")
Client = input("What is your operating system?\nRespond with 1, 2 or 3.\n1. Windows\n2. Mac\n3. Linux\n>: ")

if Client == "1":
    Client = "Windows"
if Client == "2":
    Client = "Mac"
    print("Mac is not supported yet. You may experience issues.")
if Client == "3":
    Client = "Linux"
    print("Linux is not supported yet. You may experience issues.")

print("Where shall we install StarScript?")
print("You need to input the directory location. Here we have some examples:")
print("Example: C:\\Program Files\\StarScript")
print("Example: C:\\StarScript")
print("Example: /home/user/StarScript")
InstallLocation = input("Directory:")

print("Installing Now!")

print(f"{Clear}0 % - Checking if directory exists")
if os.path.exists(InstallLocation):
    print(f"{Success}      - Directory exists")
else:
    print(f"{Error}      - Directory Doesn't Exist, Creating Now")
    os.mkdir(InstallLocation)
    print(f"{Success}      - Directory Made")

print(f"{Clear}10 % - Copying Core Components to the new Folder")

# Copy Core Folder to new Directory
try:
    shutil.copytree("Core", f"{InstallLocation}/Core")
except:
    print(f"{Success}      - Core Folder Already Exists")


print(f"{Clear}20 % - Copying Core Scripts to the new Folder")
try:shutil.copy("Core.py", f"{InstallLocation}/Core.py")
except:print(f"{Success}      - Core.py Already Exists")

try:shutil.copy("RunLine.py", f"{InstallLocation}/RunLine.py")
except:print(f"{Success}      - RunLine.py Already Exists")

try:shutil.copy("Main.py", f"{InstallLocation}/Main.py")
except:print(f"{Success}      - Main.py Already Exists")

#WindowExtension.py
try:shutil.copy("windowExtension.py", f"{InstallLocation}/windowExtension.py")
except:print(f"{Success}      - WindowExtension.py Already Exists")

print(f"{Clear}30 % - Copying Example Scripts")
try:shutil.copytree("Scripts", f"{InstallLocation}/Scripts")
except:print(f"{Success}      - Scripts Folder Already Exists")