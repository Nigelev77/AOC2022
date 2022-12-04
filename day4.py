def p1(ranges):
    pairs = 0
    for r in ranges:
        p1 = r[0]
        p2 = r[1]
        s1 = set(range(p1[0], p1[1]+1))
        s2 = set(range(p2[0], p2[1]+1))
        if(s1 <= s2 or s2<=s1):
            pairs += 1
    return pairs

def p2(ranges):
    pairs = 0
    #part 2
    for r in ranges:
        p1 = r[0]
        p2 = r[1]
        s1 = set(range(p1[0], p1[1]+1))
        s2 = set(range(p2[0], p2[1]+1))
        if(s1 & s2):
            pairs += 1
    return pairs

with open("day4.txt", "r") as file:
    ranges = []
    pairs = 0
    
    for line in file:
        line = line.strip()
        range1 = tuple(int(i) for i in line.split(",")[0].split("-"))
        range2 = tuple(int(i) for i in line.split(",")[1].split("-"))
        ranges.append((range1, range2))
    



    print(p1(ranges), p2(ranges))

