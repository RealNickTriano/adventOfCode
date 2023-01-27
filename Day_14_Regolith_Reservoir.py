
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_14_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   

def dropSand(coord, grid):
    start = coord
    rested = False
    outOfBounds = False
    tempPlace = [start[0] + 1, start[1]]
    while not rested and not outOfBounds:
        if grid[tempPlace[0]][tempPlace[1]] == '#' or grid[tempPlace[0]][tempPlace[1]] == 'o':
            tempPlace = [tempPlace[0], tempPlace[1] - 1]
            if not (0 <= tempPlace[0] < len(grid) and 0 <= tempPlace[1] < len(grid[0])):
                outOfBounds = True
                break
            elif grid[tempPlace[0]][tempPlace[1]] == '#' or grid[tempPlace[0]][tempPlace[1]] == 'o':
                tempPlace = [tempPlace[0], tempPlace[1] + 2]
                if not (0 <= tempPlace[0] < len(grid) and 0 <= tempPlace[1] < len(grid[0])):
                    outOfBounds = True
                    break
                elif grid[tempPlace[0]][tempPlace[1]] == '#' or grid[tempPlace[0]][tempPlace[1]] == 'o':
                    tempPlace = [tempPlace[0] - 1, tempPlace[1] - 1]
                    if grid[tempPlace[0]][tempPlace[1]] == '+':
                        outOfBounds = True
                        break
                    else:
                        grid[tempPlace[0]][tempPlace[1]] = 'o'
                    #print(tempPlace)
                    rested = True
        tempPlace = [tempPlace[0] + 1, tempPlace[1]]
                
    return rested and not outOfBounds

def getSandSpots(coords, colMin):
    sandCoords = []
    for i, coord in enumerate(coords):
        print(coord)
        row = int(coord[1])
        col = int(coord[0]) - colMin
        print(row, col)
        if i == 0:
            sandCoords.append([row, col])
        else:
            print('step:', i)
            print('sand coords', sandCoords)
            if sandCoords[-1][0] != row:
                spaceBetween = row - sandCoords[-1][0]
                print('compare row:', row, sandCoords[-1][0])
                print('space row:', spaceBetween)
                for i in range(abs(spaceBetween)):
                    print(i)
                    if spaceBetween < 0:
                        sandCoords.append([sandCoords[-1][0] - 1,col])
                    elif spaceBetween > 0:
                        sandCoords.append([sandCoords[-1][0] + 1, col])
                    print(sandCoords)
            elif sandCoords[-1][1] != col:
                spaceBetween = col - sandCoords[-1][1]
                print('compare col:', col, sandCoords[-1][1])
                print('space col:', spaceBetween)
                for i in range(abs(spaceBetween)):
                    if spaceBetween < 0:
                        sandCoords.append([row, sandCoords[-1][1] - 1])
                    elif spaceBetween > 0:
                        sandCoords.append([row, sandCoords[-1][1] + 1])
    print(sandCoords)         
    return sandCoords
def SolvePart2():
    return 1
    
def main():
    data = readInput()
    printList(data)
    
    coords = list(map(lambda x: list(map(lambda y: y.split(','), x.split(' -> '))), data))
    printList(coords)
    
    extraSpace = 1000
    # Build Grid
    # Get max row
    rowMax = max(list(map(lambda z: max(z), (list(map(lambda x: list(map(lambda y: int(y[1]), x)), coords))))))
    print(rowMax)
    
    # Get max col
    colMax = max(list(map(lambda z: max(z), (list(map(lambda x: list(map(lambda y: int(y[0]), x)), coords))))))
    print(colMax)
    
    # Get min col
    colMin = min(list(map(lambda z: min(z), (list(map(lambda x: list(map(lambda y: int(y[0]), x)), coords))))))
    print(colMin)
    
    # Create grid
    grid = [['.' for i in range(((colMax + 1) - colMin) + extraSpace)] for i in range(rowMax + 1 + 2)]
    
    # Set Source
    source = [0, (500 - colMin) + (extraSpace // 2)]
    grid[source[0]][source[1]] = '+'
    #printList(grid)
    
    # place all sand
    sandSpots =[]
    for item in coords:
        sandSpots = getSandSpots(item, colMin)
        for sand in sandSpots:
            grid[sand[0]][sand[1] + (extraSpace // 2)] = '#'
    grid[-1] = ['#' for i in range(((colMax + 1) - colMin) + extraSpace)]       
    printList(grid)
    
    # setup is done now drop sand until
    success = True
    units = 0
    while success:
        success = dropSand(source, grid)
        units += 1
    
    print(success)
    printList(grid)
    print(units)
    """ if not success:
        break """
    return

if __name__ == "__main__":
    main()