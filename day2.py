with open("day2.txt", "r") as file:
    moves = []
    score = 0
    for line in file:
        moves.append(line.strip().split(" "))
    for move in moves:
        move[0] = chr((ord('X')-ord('A')) + ord(move[0]))
        # score += (ord(move[1]) - ord('X')) + 1
        # diff = (ord(move[1])-ord(move[0]))
        
        # if diff == 0:
        #     score += 3
        # elif diff == 1:
        #     score += 6
        # elif diff == -2:
        #     score += 6
        end = (ord(move[1]) - ord('X'))
        score += end * 3
        if(end == 0):
            score += ((ord(move[0])-ord('X'))-1) % 3 + 1
        elif(end == 1):
            score += (ord(move[0])-ord('X')) + 1
        elif(end == 2):
            score += ((ord(move[0])-ord('X')+1)%3) + 1

    print(score)