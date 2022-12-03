def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

with open("day3.txt", "r") as file:
    rucksacks = []
    priority = 0
    for line in file:
        line = line.strip()
        rucksacks.append(line)
    for rucksack1, rucksack2, rucksack3  in grouped(rucksacks, 3):
        shared = set(rucksack1).intersection(rucksack2).intersection(rucksack3)
        for letter in shared:
            if letter.isupper():
                priority += ord(letter) - ord('A') + 27
            else:
                priority += ord(letter) - ord('a') + 1
    print(priority)


alist = [1, 2, 3, 4, 5, 6]
for x, y, z in grouped(alist, 3):
    print(f"x={x}, y={y}, z={z}")