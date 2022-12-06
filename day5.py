with open("day5.txt", "r") as file:
    stacks = {}
    data = file.read().split("\n")
    line = data.pop(0).split(' ')
    while line[0] != '-':
        stacks[int(line[0])] = [i for i in line[1:]]
        line = data.pop(0).split(' ')
    moves = []
    for line in data:
        line = line.split(' ')
        moves.append([int(line[1]), int(line[3]), int(line[5])])
    for move in moves:
        fromS = move[1]
        toS = move[2]
        x = move[0]
        # for i in range(x):
        #     stacks[toS].append(stacks[fromS].pop())
        # print(stacks)
        
        #part 2
        stacks[toS].extend(stacks[fromS][-x:])
        del stacks[fromS][len(stacks[fromS])-x:]
    res = ""
    for key, val in stacks.items():
        res += val[-1]
    print(res)