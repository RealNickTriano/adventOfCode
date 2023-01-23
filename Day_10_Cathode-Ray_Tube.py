
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_10_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   

def printCRT(display):
    
    for i, item in enumerate(display):
        print('\n', end =" ")
        for j, char in enumerate(item):
            print(char, end =" ")
    return     
def SolvePart2(cycleStates):
    
    print(200 // 40)
    print(240 % 40)
    
    crtDisplay = [[None for i in range(40)] for i in range(6)]
    #printList(crtDisplay)
    for i, cycle in enumerate(cycleStates[0:240]):
        x = cycle
        spriteCoverage = [x - 1, x, x + 1]
        if i % 40 in spriteCoverage:
            crtDisplay[i // 40][i % 40] = '#'
        else:
            crtDisplay[i // 40][i % 40] = '.'
    printCRT(crtDisplay)
    return

def main():
    data = readInput()
    #printList(data)
    
    x = 1
    cycleStates = [0 for i in range(300)]
    currentCycle = 0
    #print(cycleStates)
    for i, instruction in enumerate(data):
        if instruction == 'noop':
            cycleStates[currentCycle] = x
            currentCycle += 1
            cycleStates[currentCycle] = x
        elif instruction[0:4] == 'addx':
            cycleStates[currentCycle] = x
            currentCycle += 1
            cycleStates[currentCycle] = x
            currentCycle += 1
            x = x + int(instruction[5:])
            cycleStates[currentCycle] = x
        #print('Current Cycle: {}, X Value: {}'.format(currentCycle, x))
    
    print(sum([cycleStates[19] * 20, cycleStates[59] * 60, cycleStates[99] * 100, cycleStates[139] * 140, cycleStates[179] * 180, cycleStates[219] * 220]))
    SolvePart2(cycleStates)
    return

if __name__ == "__main__":
    main()