from tkinter import *
from tkinter import ttk, filedialog


window = Tk()
window.title('SanBot Application Importer')

def pickDirectory():
    return (filedialog.askdirectory(title="What is your folder for all your projects", initialdir="/"))

directoryButton = Button(window, text="Pick Folder", width=25, command=pickDirectory)

header = Label(window, text="Choose a directory: ")



header.grid(row=0, column=0, padx=100, pady=100)
directoryButton.grid(row=0, column=1)




window.mainloop()
