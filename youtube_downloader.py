from pytube import YouTube
from sys import argv
import tkinter

root=tkinter.Tk()

root.title("Video Downloader")
root.geometry("600x300")
root.iconbitmap("icon.ico")

startLabel =tkinter.Label(root,text="Paste YouTube link here: ")
startEntry=tkinter.Entry(root)


startLabel.pack()
startEntry.pack()

def start():
    
    link = startEntry.get()
    yt = YouTube(link)

    print("Title: ", yt.title)

    print("View: ", yt.views)

    yd = yt.streams.get_highest_resolution()

    # ADD FOLDER HERE
    yd.download('./YTfolder')

plotButton= tkinter.Button(root,text="Ok", command=start)
plotButton.pack()

root.mainloop()
