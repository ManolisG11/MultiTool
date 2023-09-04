import tkinter as tk
from tkinter import *
import os
import sys
from tkinter import messagebox


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Python MT")
        self.root.geometry("600x300")
        root.iconbitmap("icon.ico")
        root.resizable(False, False)

        self.welcome_label = tk.Label(self.root, text="Welcome", justify="center", fg="blue", font=("Arial", 24))
        self.welcome_label.place(x=230, y=40)
        
        self.button = Button(text = 'Weather', bd = '5', command=weather)
        self.button.place(x=260, y=90)

        self.button = Button(text = 'File Organizer', bd = '5', command= file_org)
        self.button.place(x=250, y=125)

        self.button = Button(text = 'Games', bd = '5', command=games)
        self.button.place(x=268, y=160)

        self.button = Button(text = 'Video Downloader', bd = '5', command=video_downloader)
        self.button.place(x=240, y=195)

        self.button = Button(text = 'Shutdown', bd = '5', command=shutdown)
        self.button.place(x=260, y=230)

def weather():
    os.system('weather_app.py')

def file_org():
    os.system('file_organizer.py')

def games():
    os.system('games.py')

def video_downloader():
     os.system('youtube_downloader.py')

def shutdown():
        a=messagebox.askyesno('Warning',"Are You sure You Want To Shotdown your Pc?")
        if a==True:
            return os.system("shutdown /s /t 1")
        
if __name__ == "__main__":
    roott = tk.Tk()
    app = Main(roott)
    roott.mainloop()
