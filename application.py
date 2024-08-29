from tkinter import *
from tkinter import ttk, filedialog
from database import *
from utils import *

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

def refreshList():
    print("test")
    deviceMenu.configure(values=upload())

def buttonCheck():
    if (dropDownMenu.get() != 'none' and deviceMenu.get() != 'none'):
        try: 
            subprocess.run(f"adb -s {deviceMenu.get()} install {dropDownMenu.get()}{rute}")
            print(f"adb -s {deviceMenu.get()} install {dropDownMenu.get()}{rute}")
        except Exception as e: 
            print(f"error: {e}")

# Initialize customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

window = customtkinter.CTk()  # Use CTk instead of Tk
window.title('SanBot Application Importer')

window.geometry("400x300")  # Set the desired width and height
window.resizable(False, False)  # Disable window resizing

# Tabview 1
tabview1 = customtkinter.CTkTabview(window, height=20) #, segmented_button_selected_color="#D3D3D3", text_color="black"
tabview1.grid(row=0, column=0, pady=(10, 5), padx=10)
tabview1.add("Choose Application")

# Tab 1 content
tab1 = tabview1.tab("Choose Application")
directoryButton = customtkinter.CTkButton(tab1, text="Pick Folder", width=200, command=pickDirectory)
dropDownMenu = customtkinter.CTkOptionMenu(tab1, command=update, variable=StringVar(value=fetchRecent()), 
values=getPopularityList(), height=30)
dropDownMenu.set(fetchRecent())

directoryButton.grid(row=1, column=0, padx=(10, 5))
dropDownMenu.grid(row=1, column=1, padx=(5, 10))

# Tabview 2
tabview2 = customtkinter.CTkTabview(window, height=20)
tabview2.grid(row=1, column=0, pady=(5, 5), padx=10)
tabview2.add("Choose Device")

# Tab 2 content
tab2 = tabview2.tab("Choose Device")
deviceMenu = customtkinter.CTkOptionMenu(tab2, values=upload(), height=30)
deviceMenu.set("none")
refreshButton = customtkinter.CTkButton(tab2, text="Refresh Devices", command=refreshList, width=200, height=30)

refreshButton.grid(row=1, column=0, padx=(10, 5))
deviceMenu.grid(row=1, column=1, padx=(5, 10))

# Tabview 3
tabview3 = customtkinter.CTkTabview(window, height=20)
tabview3.grid(row=2, column=0, padx=10,)
tabview3.add("Upload APK")

# Tab 3 content
tab3 = tabview3.tab("Upload APK")

# Center the button by using columnspan and grid settings
tab3.grid_columnconfigure(0, weight=1)  # Ensure the column expands equally
pushButton = customtkinter.CTkButton(tab3, text="Push APK", command=buttonCheck, height=30)

pushButton.grid(row=1, column=0, pady=(5, 5), padx=(10, 10), sticky="ew")

window.protocol("WM_DELETE_WINDOW", whenAppIsClosed)
window.mainloop()
