
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_9_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   
      


def chaseH(t_pos, h_pos):
    tX = t_pos[0]
    tY = t_pos[1]
    hX = h_pos[0]
    hY = h_pos[1]
    diffX = hX - tX
    diffY = hY - tY
    
    if not (diffX == 0) and not (diffY == 0):
        if diffX < 0:
            tX -= 1
        elif diffX > 0:
            tX += 1
        if diffY < 0:
            tY -= 1
        elif diffY > 0:
            tY += 1
        print((hX, hY), (tX, tY))
        return (hX, hY), (tX, tY)
    if not (diffX == 0 or diffX == 1 or diffX == -1):
        if diffX < 0:
            tX -= 1
        elif diffX > 0:
            tX += 1
            
    if not (diffY == 0 or diffY == 1 or diffY == -1):
        if diffY < 0:
            tY -= 1
        elif diffY > 0:
            tY += 1
    print((hX, hY), (tX, tY))
    return (hX, hY), (tX, tY) 

def TPosAdjacentToH(t_pos, h_pos):
    tX = t_pos[0]
    tY = t_pos[1]
    hX = h_pos[0]
    hY = h_pos[1]
    
    if (hX - 1, hY) == (tX, tY) or (hX + 1, hY) == (tX, tY):
        return True
    elif (hX, hY - 1) == (tX, tY) or (hX, hY + 1) == (tX, tY):
        return True
    elif (hX - 1, hY - 1) == (tX, tY) or (hX + 1, hY + 1) == (tX, tY) or (hX - 1, hY + 1) == (tX, tY) or (hX + 1, hY - 1) == (tX, tY):
        return True
    
    return False

def SolvePart2(dataInPairs):
    h_pos = (0,0)
    t_pos = (0,0)
    tailRopes = [(0,0) for i in range(9)]
    
    tailPositions = {(0,0)}
    for i, motion in enumerate(dataInPairs):
        direction = motion[0]
        steps = int(motion[1])
        
        for i in range(steps):
            if direction == 'R':
                h_pos = (h_pos[0] + 1, h_pos[1])
            elif direction == 'L':
                h_pos = (h_pos[0] - 1, h_pos[1])
            elif direction == 'U':
                h_pos = (h_pos[0], h_pos[1] + 1)
            elif direction == 'D':
                h_pos = (h_pos[0], h_pos[1] - 1)
            
            for j, entry in enumerate(tailRopes):
                if j == 0:
                    isAdjacent = TPosAdjacentToH(entry, h_pos)
                else:
                    isAdjacent = TPosAdjacentToH(entry, tailRopes[j - 1])
                if isAdjacent:
                    if j == 0:
                        print('Adjacent -> H, T', entry, h_pos)
                    else:
                        print('Adjacent -> H, T', entry, tailRopes[j - 1])
                else:
                    if j == 0:
                        print('Not Adjacent -> H, T', h_pos, entry)
                        h_pos, tailRopes[j] = chaseH(entry, h_pos)
                    else:
                        print('Not Adjacent -> H, T', tailRopes[j - 1], entry)
                        tailRopes[j - 1], tailRopes[j] = chaseH(entry, tailRopes[j - 1])
                        if j == 8:
                            tailPositions.add(tailRopes[j])
    print(tailPositions)
    print(len(tailPositions))            
    return

def main():
    data = readInput()
    printList(data)
    dataInPairs = list(map(lambda x: x.split(' '), data))
    printList(dataInPairs)   
    h_pos = (0,0)
    t_pos = (0,0)
    tailRopes = [(0,0) for i in range(9)]
    
    tailPositions = {(0,0)}
    for i, motion in enumerate(dataInPairs):
        direction = motion[0]
        steps = int(motion[1])
        
        for i in range(steps):
            if direction == 'R':
                h_pos = (h_pos[0] + 1, h_pos[1])
            elif direction == 'L':
                h_pos = (h_pos[0] - 1, h_pos[1])
            elif direction == 'U':
                h_pos = (h_pos[0], h_pos[1] + 1)
            elif direction == 'D':
                h_pos = (h_pos[0], h_pos[1] - 1)
            
            isAdjacent = TPosAdjacentToH(t_pos, h_pos)
            if isAdjacent:
                print('Adjacent -> H, T', h_pos, t_pos)
            else:
                print('Not Adjacent -> H, T', h_pos, t_pos)
                h_pos, t_pos = chaseH(t_pos, h_pos)
                tailPositions.add(t_pos)
    print(tailPositions)
    print(len(tailPositions))
    SolvePart2(dataInPairs)
    
    return

if __name__ == "__main__":
    main()