with open("day6.txt", "r") as file:
    data = file.read().split("\n")
    signal = data[0]
    counter = 0

    #part 1
    signalSize = 4
    setSignal = set(signal[counter:counter+signalSize])
    while len(setSignal)<signalSize:
        counter += 1
        setSignal = set(signal[counter:counter+signalSize])
    print(counter + signalSize)
    #part 2
    signalSize = 14
    counter = 0
    setSignal = set(signal[counter:counter+signalSize])
    while len(setSignal)<signalSize:
        counter += 1
        setSignal = set(signal[counter:counter+signalSize])
    
    print(counter+signalSize)
    someData = [0, 1, 2, 3, 4, 5, 5, 6, 7]
    print(*someData[1:4])