import subprocess
#Functions file

#Function for parsing dir messages.
#Do some for loop, where you take one line  and check if it has <DIR>. if it has <DIR> its a subdirectory which means we can get what ever the name is after.
#Thentake what ever the the name is into list, re print the list for the user to choose which one application he wants to publish.
#IT will insert the {application}/path-to-apk, then select the debugging file.
#Maybe make some error handling if there are multiple apk files. like choose which one. same parsin process.


# Sandbot confirmation

#   Task: 
# 1. Find if the robot is connected 
# 2. upload the code based on the argument

#   Resource: 
# 1. adb devices  -> 40100100420caa8848cf
# 2. path arg 

def upload(path): 
    try:
        connConfirmation = subprocess.run("adb devices", capture_output=True, text=True, shell=True)
    except: 
        print(f"error: {connConfirmation.stderr}")
    
    # Search feature

    

    print("test")


def parseProjectFile(message):
    dirList = []
    splitStringLines = message.splitlines()
    for x in splitStringLines:
        if "<DIR>" in x:
            splitString = x.split()
            getDirName = splitString[3:]
            fixName = " ".join(getDirName)
            # Filter out '.' and '..'
            if fixName not in ('.', '..'):
                dirList.append(fixName)
    
    print(dirList)