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
        dropDownMenu.set(parsePathName(path))
        dropDownMenu.configure(values=getPopularityList())

def whenAppIsClosed():
    close()
    window.destroy()

def refreshList():
    deviceMenu.configure(values=upload())

def show_popup_message(message):
    popup_label.configure(text=message)
    popup_frame.grid(row=3, column=0, pady=(10, 10), padx=(10, 10), sticky="ew")

def hide_popup_message():
    popup_frame.grid_forget()

def buttonCheck():
    if (dropDownMenu.get() != 'none' and deviceMenu.get() != 'none'):   
        try: 
            install = subprocess.run(f"adb -s {deviceMenu.get()} install -r {nameFetch()[0]}{rute}",
                                     capture_output=True, text=True)
            messages = install.stdout
            print(f"adb -s {deviceMenu.get()} install {dropDownMenu.get()}{rute}")
            print(messages)
            if messages:
                parsedMessages = messages.splitlines()
                for message in parsedMessages:
                    if message == "Success":
                        show_popup_message("Upload finished!")
        except Exception as e: 
            print(f"error: {e}")

def nameFetch(): return parsePathName(fetchRecent())

def ddmFIX(path):
    popList = update(path)
    dropDownMenu.set(nameFetch()[1])
    dropDownMenu.configure(values= popList)

# Initialize customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

window = customtkinter.CTk()  # Use CTk instead of Tk
window.title('SanBot Application Importer')
window.iconbitmap(r'C:\Users\larst\Downloads\NTNU.ico')

# window.geometry("400x320")  # Set the desired width and height
window.resizable(False, False)  # Disable window resizing

# Tabview 1
tabview1 = customtkinter.CTkTabview(window,
                                    height=20, 
                                    segmented_button_selected_hover_color="#3D3D3D", 
                                    segmented_button_selected_color="#3D3D3D") #, segmented_button_selected_color="#D3D3D3", text_color="black"
tabview1.grid(row=0, column=0, pady=(10, 5), padx=10)
tabview1.add("Choose Application")

# Tabview 1 changing the cursor
for tab_id in tabview1._segmented_button._buttons_dict.values():
    tab_id.configure(cursor="arrow")

# Tab 1 content
tab1 = tabview1.tab("Choose Application")
directoryButton = customtkinter.CTkButton(tab1, text="Pick Folder", width=200, command=pickDirectory)
dropDownMenu = customtkinter.CTkOptionMenu(tab1, command=ddmFIX,  values=getPopularityList(), height=30)
dropDownMenu.set(nameFetch()[1])

directoryButton.grid(row=1, column=0, padx=(10, 5))
dropDownMenu.grid(row=1, column=1, padx=(5, 10))

# Tabview 2
tabview2 = customtkinter.CTkTabview(window, 
                                    height=20,
                                    segmented_button_selected_hover_color="#3D3D3D", 
                                    segmented_button_selected_color="#3D3D3D")
tabview2.grid(row=1, column=0, pady=(5, 5), padx=10)
tabview2.add("Choose Device")

# Tabview 2 changing the cursor
for tab_id in tabview2._segmented_button._buttons_dict.values():
    tab_id.configure(cursor="arrow")

# Tab 2 content
tab2 = tabview2.tab("Choose Device")
deviceMenu = customtkinter.CTkOptionMenu(tab2, values=upload(), height=30)
deviceMenu.set("none")
refreshButton = customtkinter.CTkButton(tab2, text="Refresh Devices", command=refreshList, width=200, height=30)

refreshButton.grid(row=1, column=0, padx=(10, 5))
deviceMenu.grid(row=1, column=1, padx=(5, 10))

# Tabview 3
tabview3 = customtkinter.CTkTabview(window, 
                                    height=20,
                                    segmented_button_selected_hover_color="#3D3D3D", 
                                    segmented_button_selected_color="#3D3D3D")
tabview3.grid(row=2, column=0, padx=10,)
tabview3.add("Upload APK")

# Tabview 2 changing the cursor
for tab_id in tabview3._segmented_button._buttons_dict.values():
    tab_id.configure(cursor="arrow")

# Tab 3 content
tab3 = tabview3.tab("Upload APK")

# Center the button by using columnspan and grid settings
tab3.grid_columnconfigure(0, weight=1)  # Ensure the column expands equally
pushButton = customtkinter.CTkButton(tab3, text="Push APK", command=buttonCheck, height=30)

pushButton.grid(row=1, column=0, pady=(5, 5), padx=(10, 10), sticky="ew")

#    Popup message   #
popup_frame = customtkinter.CTkFrame(window)
popup_label = customtkinter.CTkLabel(popup_frame, text="")
popup_label.pack(pady=20)
close_button = customtkinter.CTkButton(popup_frame, text="Close", command=hide_popup_message)
close_button.pack(pady=10)

# Initially hide the popup frame
popup_frame.grid_forget()


window.protocol("WM_DELETE_WINDOW", whenAppIsClosed)
window.mainloop()
