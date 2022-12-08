with open("day8.txt", "r") as file:
    trees = [[int(i) for i in line] for line in file.read().splitlines()]
    treesT = (list(map(list, zip(*trees))))
    visible = len(trees)*2 + len(trees[0])*2 - 4
    
    visibleTrees = set()
    for index, row in enumerate(trees[1:len(trees)-1]):
        p1, p2 = 1, len(row)-2
        maxL, maxR = row[0], row[len(row)-1]        
        while p1 < len(row)-1:
            if row[p1] > maxL:
                pos = (index+1, p1)
                if pos not in visibleTrees:
                    visible += 1
                    visibleTrees.add(pos)
                maxL = row[p1]
            p1 += 1
        while p2 > 0:
            if row[p2] > maxR:
                pos = (index+1, p2)
                if pos not in visibleTrees:
                    visible += 1
                    visibleTrees.add(pos)
                maxR = row[p2]
            p2 -= 1
    
    for index, row in enumerate(treesT[1:len(trees)-1]):
        p1, p2 = 1, len(row)-2
        maxL, maxR = row[0], row[len(row)-1]        
        while p1 < len(row)-1:
            if row[p1] > maxL:
                pos = (p1, index+1)
                if pos not in visibleTrees:
                    visible += 1
                    visibleTrees.add(pos)
                maxL = row[p1]
            p1 += 1
        while p2 > 0:
            if row[p2] > maxR:
                pos = (p2, index+1)
                if pos not in visibleTrees:
                    visible += 1
                    visibleTrees.add(pos)
                maxR = row[p2]
            p2 -= 1
    
    maxScore = 0
    for visibleTree in visibleTrees:
        height = trees[visibleTree[0]][visibleTree[1]]
        up, down, left, right = visibleTree[1], visibleTree[1], visibleTree[0], visibleTree[0]
        blocked = False
        while up >= 0 and not blocked:
            up -= 1
            if up == 0:
                break
            h = trees[visibleTree[0]][up]
            if h >= height:
                blocked = True
        blocked = False
        while down <= len(trees)-1 and not blocked:
            down += 1
            if down == len(trees)-1:
                break
            h = trees[visibleTree[0]][down]
            if h >= height:
                blocked = True
        blocked = False
        while left >= 0 and not blocked:
            left -= 1
            if left == 0:
                break
            h = trees[left][visibleTree[1]]
            if h >= height:
                blocked = True
        blocked = False
        while right <= len(trees[0])-1 and not blocked:
            right += 1
            if right == len(trees[0])-1:
                break
            h = trees[right][visibleTree[1]]
            if h >= height:
                blocked = True
        vu = visibleTree[1] - up
        vd = down - visibleTree[1]
        vl = visibleTree[0] - left
        vr = right - visibleTree[0]
        score = vu * vd * vl * vr
        if score > maxScore:
            maxScore = score
            print(f"The tree with highest curr is {visibleTree}")

    print(visible)
    print(maxScore)



    