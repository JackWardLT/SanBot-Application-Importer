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

# Frame 1
frame1 = customtkinter.CTkFrame(window, height=40)
directoryButton = customtkinter.CTkButton(frame1, text="Pick Folder", width=200, command=pickDirectory)
dropDownMenu = customtkinter.CTkOptionMenu(frame1, command=update, variable=StringVar(value=fetchRecent()), 
                                           values=getPopularityList())
dropDownMenu.set(fetchRecent())

padding= 20
directoryButton.grid(row=1, column=0, padx=(10, 5), pady=(padding, 10))
dropDownMenu.grid(row=1, column=1, padx=(5, 10), pady=(padding, 10))

# Frame 2
frame2 = customtkinter.CTkFrame(window)
label2 = customtkinter.CTkLabel(frame2, text="TEXT", anchor="center")
deviceMenu = customtkinter.CTkOptionMenu(frame2, values=upload())
deviceMenu.set("none")
refreshButton = customtkinter.CTkButton(frame2, text="Refresh Devices", command=refreshList, width=200)

label2.grid(row=0, column=0, columnspan=2, pady=(10, 5))
refreshButton.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
deviceMenu.grid(row=1, column=1, padx=(5, 10), pady=(10, 5))

# Frame 3
frame3 = customtkinter.CTkFrame(window)
label3 = customtkinter.CTkLabel(frame3, text="TEXT", anchor="center")
pushButton = customtkinter.CTkButton(frame3, text="Push APK", command=buttonCheck)

label3.grid(row=0, column=0, pady=(10, 5))
pushButton.grid(row=1, column=0, pady=(5, 10), padx=(10, 10))

# Place frames
frame1.grid(row=0, column=0, pady=(22, 5), padx=10,)
frame2.grid(row=1, column=0, pady=(5, 5), padx=10)
frame3.grid(row=2, column=0, pady=(5, 10), padx=10)

# Overlapping frame
overlappingFrame1 = customtkinter.CTkFrame(window, height=70, width=300, fg_color="transparent", border_width=0, corner_radius=20)  # Adjust size and color
label4 = customtkinter.CTkLabel(overlappingFrame1, text="Choose Project", anchor="center")
label4.pack(padx=10, pady=2)  # Add padding to ensure text visibility

# Position the overlapping frame with a gap above it
overlappingFrame1.place(x=145, y=2)  # Adjust x and y to control the gap

window.protocol("WM_DELETE_WINDOW", whenAppIsClosed)
window.mainloop()
