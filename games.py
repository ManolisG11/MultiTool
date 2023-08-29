import tkinter as tk
from tkinter import *
from AppOpener import open
import webbrowser

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Games")
        self.root.geometry("600x300")

        self.online_label = tk.Label(self.root, text="Games", justify="center", fg="blue", font=("Arial", 24))
        self.online_label.place(x=230, y=40)

        self.button = Button(text = 'Minecraft Launcher', bd = '5', command=minecraftOpen)
        self.button.place(x=240, y=90)

        self.button = Button(text = 'Asphalt Legends 9', bd = '5', command=asphaltOpen)
        self.button.place(x=120, y=90)

        self.button = Button(text = 'Roblox', bd = '5', command=robloxOpen)
        self.button.place(x=370, y=90)

        self.online_label = tk.Label(self.root, text="Online Games", justify="center", fg="blue", font=("Arial", 24))
        self.online_label.place(x=190   , y=130)

        self.button = Button(text = 'Roblox (Web)', bd = '5', command=robloxWebOpen)
        self.button.place(x=240, y=180)

        self.button = Button(text = 'Poki', bd = '5', command=pokiOpen)
        self.button.place(x=200, y=180)

        self.button = Button(text = 'Friv', bd = '5', command=frivOpen)
        self.button.place(x=329, y=180)

def minecraftOpen():
    open("minecraft_launcher")

def asphaltOpen():
    open("asphalt_legends")

def robloxOpen():
    open("roblox_player")

def robloxWebOpen():
    webbrowser.open('https://roblox.com')

def pokiOpen():
    webbrowser.open('http://poki.gr')

def frivOpen():
    webbrowser.open('http://friv.com') 

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()