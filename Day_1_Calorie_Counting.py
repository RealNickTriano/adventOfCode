def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    elvesCounts = []
    with open('Day_1_input.txt', 'r') as f:
        read_data = f.read()
        print(read_data)
        counts = read_data.split('\n')
        print(counts)
        elfCount = 0
        for i, item in enumerate(counts):
            print(item)
            if item == '':
                elvesCounts.append(elfCount)
                elfCount = 0
            else:
                elfCount += int(item)
                
    return elvesCounts

def SolvePart2(elvesCals):
    first = 0
    second = 0
    third = 0

    for i, item in enumerate(elvesCals):
        if item > first:
            third = second
            second = first
            first = item
        elif item > second:
            third = second
            second = item
        elif item > third:
            third = item
    
    print(first, second, third)
    print(sum([first, second, third]))
    return

def main():
    elvesCals = readInput()
    printList(elvesCals)
    
    max = 0
    index = 0
    for i, item in enumerate(elvesCals):
        if item > max:
            max = item
            index = i
    
    print(max, index + 1)
    
    SolvePart2(elvesCals)
    
if __name__ == "__main__":
    main()