
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_4_input.txt', 'r') as f:
        read_data = f.read()
        data = read_data.split('\n')
        print(data)
        
    return data

def SolvePart2(cleanedInput):
    overlap = 0
    for item in cleanedInput:
        intItem = list(map(int, item))
        a = intItem[0]
        b = intItem[1]
        c = intItem[2]
        d = intItem[3]
        if (c >= a and c <= b) or (a >= c and a <= d) or (a >= c and a <= d) or (b >= c and b <= d):
            print(intItem)
            overlap += 1
            
    
    print(overlap)
    return

def clean(item):
    sections = item.split(',')
    #print(sections)
    a, b = sections[0].split('-')
    c, d = sections[1].split('-')
    #print([a, b, c, d])
    return [a, b, c, d]
    
def main():
    # 2-4, 6-8 -> a-b, c-d
    # If c <= b then the two sections overlap
    # find how many fully contain eachother
    # fully contain condition:
    # If (c >= a and d <= b) or (a >= c and b <= d)
    input = readInput()
    printList(input)
    fullyContained = 0
    
    cleanedInput = list(map(clean, input))
    printList(cleanedInput)
    print('newLine!')
    
    for item in cleanedInput:
        intItem = list(map(int, item))
        a = intItem[0]
        b = intItem[1]
        c = intItem[2]
        d = intItem[3]
        if (c >= a and d <= b) or (a >= c and b <= d):
            print(intItem)
            fullyContained += 1
            
    
    print(fullyContained)
    
    SolvePart2(cleanedInput)
    return

if __name__ == "__main__":
    main()