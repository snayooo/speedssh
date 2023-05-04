import subprocess
from tkinter import *
import webbrowser
import os
import time
import json
import pyautogui

root = Tk()

with open("servers.json", "w") as file:
    file.write('[{"servers": "True"}]')

def donothing():
    nothing = Toplevel(root)
    button = Button(nothing, text="Do nothing button")
    button.pack()

def helpGithub():
    webbrowser.open("https://github.com/snayooo")

def helpPypi():
    webbrowser.open("")

def serverServermanager():
    filewin = Toplevel(root)
    label1 = Label(filewin, text="Servermanager").pack()

def serverAddServer():
    filewin = Toplevel(root)
    filewin['bg'] = '#2e2e2e'
    filewin.geometry("500x300")
    filewin.title("SpeedSSH - Add server")

    title = Label(filewin, text="Add Server", font=('default 22 bold'), bg='#2e2e2e', fg='#ffffff').pack()
    nameLabel = Label(filewin, text="Servername: ", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    nameInput = StringVar()
    nameEntry = Entry(filewin, textvariable=nameInput).pack()
    ipLabel = Label(filewin, text="IP address: ", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    ipInput = StringVar()
    ipEntry = Entry(filewin, textvariable=ipInput).pack()
    portLabel = Label(filewin, text="Port :", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    portInput = StringVar()
    portEntry = Entry(filewin, textvariable=portInput).pack()
    userLabel = Label(filewin, text="User: ", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    userInput = StringVar()
    userEntry = Entry(filewin, textvariable=userInput).pack()
    passwdLabel = Label(filewin, text="Password: ", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    passwdInput = StringVar()
    passwdEntry = Entry(filewin, textvariable=passwdInput).pack()

    def saveData():

        servername = nameInput.get()
        ip = ipInput.get()
        port = portInput.get()
        user = userInput.get()
        passwd = passwdInput.get()
        command = "ssh " + user + "@" + ip + ":" + port

        with open("servers.json", "r") as json_file:
            exisitng_data = json.load(json_file)

        new_data = [
            {
            'servername': servername,
            'ip_address': ip,
            'command': command
            },
        ]

        exisitng_data.extend(new_data)
        with open("servers.json", "w") as json_file:
            json.dump(exisitng_data, json_file)

        time.sleep(1)

        filewin.destroy()



    button = Button(filewin, text="Add Server", font=12, command=saveData).pack(pady=12)

def serverQuickConnect():
    quickconnect = Toplevel(root)
    quickconnect['bg'] = "#2e2e2e"
    quickconnect.geometry("500x400")
    quickconnect.title("SpeedSSH - Quick connect")
    title = Label(quickconnect, text="Quick connect", font=('default 22 bold'), bg='#2e2e2e', fg='#ffffff').pack()
    ipLabel = Label(quickconnect, text="IP address: ", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    ipInput = StringVar()
    ipEntry = Entry(quickconnect, textvariable=ipInput).pack()
    portLabel = Label(quickconnect, text="Port :", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    portInput = StringVar()
    portEntry = Entry(quickconnect, textvariable=portInput).pack()
    userLabel = Label(quickconnect, text="User: ", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    userInput = StringVar()
    userEntry = Entry(quickconnect, textvariable=userInput).pack()
    passwdLabel = Label(quickconnect, text="Password: ", font=14, bg='#2e2e2e', fg='#ffffff').pack()
    passwdInput = StringVar()
    passwdEntry = Entry(quickconnect, textvariable=passwdInput).pack()

    def connect():

        ip = ipInput.get()
        port = portInput.get()
        user = userInput.get()
        passwd = passwdInput.get()
        command = "ssh " + user + "@" + ip + ":" + port

    button = Button(quickconnect, text="Connect", command=connect).pack()



root.title("SpeedSSH")
root.geometry("700x500")
root['bg'] = '#2e2e2e'

menubar = Menu(root)
servermenu = Menu(menubar, tearoff=0)
servermenu.add_command(label="Servermanager", command=serverServermanager)
servermenu.add_separator()
servermenu.add_command(label="Add server", command=serverAddServer)
servermenu.add_command(label="Copy IP address", command=donothing)
servermenu.add_command(label="Remove server", command=donothing)
servermenu.add_separator()
servermenu.add_command(label="Quick connect", command=serverQuickConnect)
servermenu.add_command(label="Ping", command=donothing)
servermenu.add_separator()
servermenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Server", menu=servermenu)

settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label="Settings", command=donothing)
menubar.add_cascade(label="Settings", menu=settingsmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="GitHub", command=helpGithub)
helpmenu.add_separator()
helpmenu.add_command(label="PyPi", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

with open("servers.json", "r") as file:
    print()

servers = "False"

if servers == "True":
    for i in range(1):
        with open("servers.json", "r") as json_file:
            data = json.load(json_file)
            serverName = data[0]["servername"]

    serverList = Label(root, text=serverName, bg='#2e2e2e', font=14, fg="#ffffff").pack()

else:
    print("Servers are undefined")

root.config(menu=menubar)
root.mainloop()