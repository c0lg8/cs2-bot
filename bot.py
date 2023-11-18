import wmi
import os
import time

count = 0

f = wmi.WMI()

def notRunning():
    os.system('cls')
    print('Cities Skylines 2 is not running')
    time.sleep(1)
    checkIfRunning()

def running():
    exit()

def checkIfRunning():
    global count
    for process in f.Win32_Process():
        if process.Name == 'Cities2.exe':
            print("Cities Skylines 2 is running")
            count += 1
    if count > 0:
        running()
    elif count <= 0:
        notRunning()

checkIfRunning()