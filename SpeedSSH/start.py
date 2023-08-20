import time
import subprocess

print(" ____  ____  ____  ____  ____  ____  ____  _  _  ")
print("/ ___)(  _ \(  __)(  __)(    \/ ___)/ ___)/ )( \ ")
print("\___ \ ) __/ ) _)  ) _)  ) D (\___ \\___ \) __ ( ")
print("(____/(__)  (____)(____)(____/(____/(____/\_)(_/ ")
print("\nSpeedSSH v. 1.0.0")
print("Copyright © - Snayo 2023")

time.sleep(1)

print("\nWhich operating system are you using?")
print("1 : Windows")
print("2: MacOS")

os = int(input("\nEnter a number: "))

if os == 1:
    subprocess.call("/windows.py")
elif os == 2:
    subprocess.call("/macos.py")
else:
    print("ERROR")
    exit