import subprocess
#Functions file
rute = r"\app\build\outputs\apk\debug\app-debug.apk"

def upload(path): 
    getDevices = subprocess.run("adb devices", capture_output=True, text=True, shell=True)
    devices = parseAdbDevices(getDevices.stdout)     
    device = chooseFromList(devices)   
    try: 
        subprocess.run(f"adb -s {device} install {path}{rute}")
    except Exception as e: 
        print(f"error: {e}")

def parseAdbDevices(message): 
    devices = []
    splitStringes = message.splitlines()
    splitStringes = " ".join(splitStringes).split()
    for index, line in enumerate(splitStringes): 
        if line == "device":
            devices.append(splitStringes[index-1])
    return devices

def parseProjectFile(message):
    dirList = []
    splitStringLines = message.splitlines()
    for line in splitStringLines:
        if "<DIR>" in line:
            fixName = " ".join(line.split()[3:])
            if fixName not in ('.', '..'):
                dirList.append(fixName)
    return dirList

def chooseFromList(list):
    index = 0
    print(f"Choose a project to upload: ")
    for application in list:
        index += 1
        print(f"[{index}] - {application}")
    return (list[int(input("Which one do you choose: "))-1])
