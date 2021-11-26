#os modulu
import os
print(os.name)

if os.name!="nt":
    print("sorry, you need windows")
else:
    print("hoş geldiniz")
print(os.getcwd())
#os.makedirs("C:\\Users\oerkan\AppData\Local\Programs\Python\Python37\OsmanWorks")

import sys
print(sys.version)

import subprocess
#subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#subprocess.call("C:\Program Files\Google\Google Earth Pro\client\googleearth.exe")
#subprocess.call('notepad.exe') #win32 dizininde 

import webbrowser
#webbrowser.open("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

from tkinterweb import HtmlFrame #import the HTML browser
try:
  import tkinter as tk #python3
except ImportError:
  import tkinter as tk #python2

root = tk.Tk() #create the tkinter window
frame = HtmlFrame(root) #create HTML browser

frame.load_website("http://tkhtml.tcl.tk/tkhtml.html") #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()






