import time
import os
import wmi

f = wmi.WMI()

flag = 0

activity = ''

def checkIfRunning():
    global activity
    activity = 'Checking Game Status'
    for process in f.Win32_Process():
        if "Cities2.exe" == process.Name:
            print("CS2 is running")
            flag = 1

    if flag == 0:
        print("CS2 is not running")

while True:
    activity = 'idle'
    checkIfRunning()
    print(activity)
    time.sleep(1)
    os.system('cls')