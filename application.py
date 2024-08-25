from tkinter import *
from tkinter import ttk, filedialog
from database import *
import customtkinter

def pickDirectory():
    print("pickDirectory function called\n")
    print(fetchRecent())
    path = filedialog.askdirectory(title="What is your folder for all your projects", initialdir="/")
    if path:
        print(f"Selected directory: {path}\n")
        update(path)
        print(fetchRecent())
        dropDownMenu.set(fetchRecent())
        dropDownMenu.configure(values=getPopularityList())

def whenAppIsClosed():
    close()
    window.destroy()


# Initialize customtkinter
customtkinter.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

window = customtkinter.CTk()  # Use CTk instead of Tk
window.title('SanBot Application Importer')

directoryButton = customtkinter.CTkButton(window, text="Pick Folder", width=200, command=pickDirectory)

dropDownMenu = customtkinter.CTkOptionMenu(window, command=update, variable=StringVar(value=fetchRecent()), 
                                           values=getPopularityList())
dropDownMenu.set(fetchRecent())

dropDownMenu.grid(row=0, column=2, padx=40)
directoryButton.grid(row=0, column=1)


window.protocol("WM_DELETE_WINDOW", whenAppIsClosed)
window.mainloop()
