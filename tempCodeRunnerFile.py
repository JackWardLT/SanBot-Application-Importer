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

    if len(charToName) > 15:
        fix = ''.join(charToName[::-1])
        return ''.join(fix) + "..."
    
    return ''.join(charToName[::-1])

print(f"result: {parsePathName("lol\\walllllahhhhababababbibibi")}")