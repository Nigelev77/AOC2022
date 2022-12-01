with open("day1.txt", "r") as file:
    calories = [0]
    size = 0
    for line in file:
        calorie = line.strip()
        if calorie == "":
            calories.append(0)
            size += 1
        else:
            calories[size] += int(calorie)
    #part 1
    print(max(calories))
    
    #part 2
    sortedCalories = sorted(calories, reverse=True)
    print(sortedCalories[0] + sortedCalories[1] + sortedCalories[2])