
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_5_input.txt', 'r') as f:
        read_data = f.read()
        data = read_data.split('\n')
        print(data[10:])
        
    return data[10:]

def SolvePart2(data):
    stacks = [['C', 'Q', 'B'],
              ['Z', 'W', 'Q', 'R'],
              ['V', 'L', 'R', 'M', 'B'],
              ['W', 'T','V', 'H', 'Z', 'C'],
              ['G', 'V', 'N', 'B', 'H', 'Z', 'D'],
              ['Q', 'V', 'F', 'J', 'C', 'P', 'N', 'H'],
              ['S', 'Z', 'W', 'R', 'T', 'G', 'D'],
              ['P', 'Z', 'W', 'B', 'N', 'M', 'G', 'C'],
              ['P', 'F', 'Q', 'W', 'M', 'B', 'J', 'N'],]
    
    for item in stacks:
        item.reverse()
    """ printList(stacks) """
    print('SOLVING PART 2')
    for i, item in enumerate(data): 
        splitArr = item.split(' ')
        amountToMove = int(splitArr[1])
        moveFrom = int(splitArr[3])
        moveTo = int(splitArr[5])
        cratesToMove = []
        #print(amountToMove, moveFrom, moveTo)
        for i in range(amountToMove):
            cratesToMove.append(stacks[moveFrom - 1].pop())
        cratesToMove.reverse()
        
        for i in range(amountToMove):
            stacks[moveTo - 1].append(cratesToMove[i])
        print('')
        printList(stacks)
    
    for item in stacks:
        print(item.pop())
    
    return
    
def main():
    """
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
    """
    stacks = [['C', 'Q', 'B'],
              ['Z', 'W', 'Q', 'R'],
              ['V', 'L', 'R', 'M', 'B'],
              ['W', 'T','V', 'H', 'Z', 'C'],
              ['G', 'V', 'N', 'B', 'H', 'Z', 'D'],
              ['Q', 'V', 'F', 'J', 'C', 'P', 'N', 'H'],
              ['S', 'Z', 'W', 'R', 'T', 'G', 'D'],
              ['P', 'Z', 'W', 'B', 'N', 'M', 'G', 'C'],
              ['P', 'F', 'Q', 'W', 'M', 'B', 'J', 'N'],]
    
    for item in stacks:
        item.reverse()
        
    printList(stacks)
    data = readInput()
    
    for i, item in enumerate(data): 
        splitArr = item.split(' ')
        amountToMove = int(splitArr[1])
        moveFrom = int(splitArr[3])
        moveTo = int(splitArr[5])
        #print(amountToMove, moveFrom, moveTo)
        for i in range(amountToMove):
            crate = stacks[moveFrom - 1].pop()
            stacks[moveTo - 1].append(crate)
        print('')
        printList(stacks)
    
    for item in stacks:
        print(item.pop())
    
    SolvePart2(data)
    return

if __name__ == "__main__":
    main()