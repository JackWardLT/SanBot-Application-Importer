from tkinter import *
from tkinter import ttk, filedialog
from database import *

def pickDirectory():
    print("pickDirectory function called\n")
    path = filedialog.askdirectory(title="What is your folder for all your projects", initialdir="/")
    if path:
        print(f"Selected directory: {path}\n")
        addPathSQL(path)
        # SQL FETCH TEST, TOMMOROW WHY DO I FETCH SO MANY!!!!
        fetched_data = fetchPathData('DIR')
        print(f"Fetched data: {fetched_data}\n")

window = Tk()
window.title('SanBot Application Importer')

directoryButton = Button(window, text="Pick Folder", width=25, command=pickDirectory)
header = Label(window, text="Choose a directory: ")

header.grid(row=0, column=0, padx=100, pady=100)
directoryButton.grid(row=0, column=1)

window.protocol("WM_DELETE_WINDOW", lambda: (closeConnection(), window.destroy()))
window.mainloop()