from tkinter import *
from tkinter import ttk, filedialog
from database import *
import customtkinter

def pickDirectory():
    print("pickDirectory function called\n")
    path = filedialog.askdirectory(title="What is your folder for all your projects", initialdir="/")
    if path:
        print(f"Selected directory: {path}\n")
        addPathSQL(path)
        print(f"Fetched data: {fetchPathData()}\n")
        header.configure(text=f"{dirLabel()}")

def dirLabel():
    return "Choose Directory" if dirCounter() else fetchPathData()
    

# Initialize customtkinter
customtkinter.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

window = customtkinter.CTk()  # Use CTk instead of Tk
window.title('SanBot Application Importer')

directoryButton = customtkinter.CTkButton(window, text="Pick Folder", width=200, command=pickDirectory)
header = customtkinter.CTkLabel(window, text=f"{dirLabel()}")


header.grid(row=0, column=0, padx=100, pady=100)
directoryButton.grid(row=0, column=1)

window.mainloop()