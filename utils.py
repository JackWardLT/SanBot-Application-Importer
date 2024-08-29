import subprocess

rute = r"\app\build\outputs\apk\debug\app-debug.apk"

def upload(): 
    getDevices = subprocess.run("adb devices", capture_output=True, text=True, shell=True)
    print("ADB Output:", getDevices.stdout)  # Debug print to see the output of adb devices
    devices = parseAdbDevices(getDevices.stdout)
    if not devices:
        print("No devices found")
    else:
        print("Found devices:", devices)
    return devices

def parseAdbDevices(message): 
    devices = []
    splitStringes = message.splitlines()
    splitStringes = " ".join(splitStringes).split()
    for index, line in enumerate(splitStringes): 
        if line == "device": # Later make pop up if the devices is offline
            devices.append(splitStringes[index-1])
    return devices

def parsePathName(path):
    if not path:
        return "none"
    
    status = True
    charToName = []
    reverseString = path[::-1]
    
    for char in reverseString:
        if char == "\\" or char == "/":
            break
        charToName.append(char)
    
    return ''.join(charToName[::-1])
