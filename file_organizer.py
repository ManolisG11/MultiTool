import os
import shutil
import tkinter

root=tkinter.Tk()

root.title("File Organizer")
root.geometry("600x300")
root.iconbitmap("icon.ico")

startLabel =tkinter.Label(root,text="Enter Path: ")
startEntry=tkinter.Entry(root)


startLabel.pack()
startEntry.pack()

def start():
    
    path = startEntry.get()
    files = os.listdir(path)
    
    for file in files:
        filename,extension = os.path.splitext(file)
        extension = extension[1:]
        if os.path.exists(path + "/" + extension):
            shutil.move(path + "/" + file,path + "/" + extension + "/" + file)
        else:
            os.makedirs(path + "/" + extension)
            shutil.move(path + "/" + file,path + "/" + extension)


plotButton= tkinter.Button(root,text="Ok", command=start)
plotButton.pack()

root.mainloop()


