from collections import defaultdict




with open("day7.txt", "r") as file:
    dirSize = defaultdict(int)
    dirLinks = defaultdict(set)
    curDir = ""
    commands = file.read().split("\n")
    for command in commands:
        if command[0] == '$':
            if command == "$ ls":
                continue
            linCom, arg = command[2:].split(" ")
            if linCom == "cd":
                if arg == "/":
                    curDir = "/"
                    continue
                if arg == "..":
                    dirs = curDir.split("/")
                    dirs.pop()  
                    if len(dirs) == 1:
                        curDir = "/"
                    else:
                        curDir = "/".join(dirs)
                else:
                    if curDir == "/":
                        curDir = "/" + arg
                    elif curDir != "":
                        curDir = curDir + "/" + arg
                    else:
                        curDir = "/"
        elif "dir " in command:
            if curDir != "/":
                dirLinks[curDir].add(curDir + "/" + command[4:])
            else:
                dirLinks[curDir].add(curDir + command[4:])
        else:
            args = command.split(" ")
            size = int(args[0])
            dirSize[curDir] += size


    total = 0
    dirKeys = []
    for key in dirLinks.keys():
        dirKeys.append(key)
    dirKeys.sort(key=lambda x:len(x.split("/")), reverse=True)
    for directory in dirKeys:
        if directory == "/":
            continue
        subDirs = dirLinks[directory]
        
        for subDir in subDirs:
            dirSize[directory] += dirSize[subDir]
    unused = 30000000
    space = 70000000

    for key, val in dirSize.items():
        if val <= 100000:
            total += val
    print(total)
    #part 2
    for subDir in dirLinks["/"]:
        dirSize["/"] += dirSize[subDir]
    used = dirSize["/"]
    needToFree = unused - (space-used)
    keys = []
    for key in dirSize.keys():
        keys.append(key)
    print(f"In use: {used}")
    print(f"Need to free at least {needToFree}")
    keys.sort(key=lambda x:len(x.split("/")), reverse=True)
    for key in keys:
        if key == "/":
            continue
        size = dirSize[key]
        if size >= needToFree:
            print(f"Deleting {key} = {size} bytes would free up enough space")

    
        
#2131559
#