rute1 = r"\app\build\outputs\apk\debug\app-debug.apk"

def parsePathName(path):
    if not path:
        return "none"
    
    status = True
    charToName = []
    reverseString = path[::-1]
    
    for char in reverseString:
        if char == "\\":
            break
        charToName.append(char)
    print(''.join(charToName[::-1]))
    
    return ''.join(charToName[::-1])

print(f"output: {parsePathName(rute1)}")