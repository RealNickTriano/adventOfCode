
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_6_input.txt', 'r') as f:
        read_data = f.read()
        print(read_data)
        
    return read_data

def allDiff(string):
    myDict = {}
    for item in string:
        if item in myDict:
            return False
        else:
            myDict[item] = item
    return True    
    
def SolvePart2(data):
    buffer = data[0:14]
    start = 0
    end = 14
    charsProcessed = 14
    print(buffer)
    while not allDiff(buffer):
        start += 1
        end += 1
        charsProcessed += 1
        buffer = data[start:end]
        print(buffer)
    
    print(buffer, charsProcessed) 
    return
    
def main():
    data = readInput()
    buffer = data[0:4]
    start = 0
    end = 4
    charsProcessed = 4
    print(buffer)
    while not allDiff(buffer):
        start += 1
        end += 1
        charsProcessed += 1
        buffer = data[start:end]
        print(buffer)
    
    print(buffer, charsProcessed)  
    SolvePart2(data)
    return

if __name__ == "__main__":
    main()