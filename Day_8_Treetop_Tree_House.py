
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_8_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   
      
def SolvePart2(grid):
    colLength = len(grid)
    rowLength = len(grid[0])
    outsideTrees = (len(grid) * 2) + (len(grid[0]) * 2) - 4
    visibleTreeCount = outsideTrees
    allScenicScores = []
    for i, row in enumerate(grid):
        for j, height in enumerate(row):
            if boundary(i, j, grid):
                print("boundary: {},{}, {}".format(i, j, height))
                # UP
                upScore = 0
                upY = i
                upX = j
                while upY > 0:
                    upY -= 1
                    upScore += 1
                    if height <= grid[upY][upX]:
                        upVisible = False 
                        
                # DOWN
                downScore = 0
                downY = i
                downX = j
                while downY < colLength - 1:
                    downY += 1
                    downScore += 1
                    if height <= grid[downY][downX]:
                        downVisible = False
                        
                # LEFT
                leftScore = 0
                leftY = i
                leftX = j
                while leftX > 0:
                    leftX -= 1
                    leftScore += 1
                    if height <= grid[leftY][leftX]:
                        leftVisible = False
                        
                # RIGHT
                rightScore = 0
                rightY = i
                rightX = j
                while rightX < rowLength - 1:
                    rightX += 1
                    rightScore += 1
                    if height <= grid[rightY][rightX]:
                        rightVisible = False
                        
            else:
                print("not boundary: {},{}, {}".format(i, j, height))    
                # UP
                upVisible = True
                upScore = 0
                upY = i
                upX = j
                while upY > 0 and upVisible:
                    upY -= 1
                    upScore += 1
                    if height <= grid[upY][upX]:
                        upVisible = False 
                        
                # DOWN
                downVisible = True
                downScore = 0
                downY = i
                downX = j
                while downY < colLength - 1 and downVisible:
                    downY += 1
                    downScore += 1
                    if height <= grid[downY][downX]:
                        downVisible = False
                        
                # LEFT
                leftVisible = True
                leftScore = 0
                leftY = i
                leftX = j
                while leftX > 0 and leftVisible:
                    leftX -= 1
                    leftScore += 1
                    if height <= grid[leftY][leftX]:
                        leftVisible = False
                        
                # RIGHT
                rightVisible = True
                rightScore = 0
                rightY = i
                rightX = j
                while rightX < rowLength - 1 and rightVisible:
                    rightX += 1
                    rightScore += 1
                    if height <= grid[rightY][rightX]:
                        rightVisible = False
                        
            
            scenicScore = upScore * downScore * rightScore * leftScore
            allScenicScores.append(scenicScore)
    
    printList(allScenicScores)      
    print(max(allScenicScores))                  
    return

def boundary(i, j, grid):
    colLength = len(grid)
    rowLength = len(grid[0])
    if i == 0 or i == colLength - 1:
        return True
    if j == 0 or j == rowLength - 1:
        return True
    return False


def main():
    data = readInput()
    printList(data)
    grid = []
    for entry in data:
        row = list(map(int, entry))
        grid.append(row)
    print('GRID:')
    printList(grid)
    
    outsideTrees = (len(grid) * 2) + (len(grid[0]) * 2) - 4
    print('OUTSIDE TREES VISIBLE:', outsideTrees)
    
    colLength = len(grid)
    rowLength = len(grid[0])
    visibleTreeCount = outsideTrees
    for i, row in enumerate(grid):
        for j, height in enumerate(row):
            if boundary(i, j, grid):
                print("boundary: {},{}, {}".format(i, j, height))
            else:
                print("not boundary: {},{}, {}".format(i, j, height))
                # Check up, down, left, right all the way
                # If any are higher or equal 
                    # not visible from that direction
                    
                # UP
                upVisible = True
                upScore = 1
                upY = i
                upX = j
                while upY > 0 and upVisible:
                    upY -= 1
                    if height <= grid[upY][upX]:
                        upVisible = False 
                    else:
                        upScore += 1
                # DOWN
                downVisible = True
                downScore = 1
                downY = i
                downX = j
                while downY < colLength - 1 and downVisible:
                    downY += 1
                    if height <= grid[downY][downX]:
                        downVisible = False
                    else:
                        downScore += 1
                # LEFT
                leftVisible = True
                leftScore = 1
                leftY = i
                leftX = j
                while leftX > 0 and leftVisible:
                    leftX -= 1
                    if height <= grid[leftY][leftX]:
                        leftVisible = False
                    else:
                        leftScore += 1
                # RIGHT
                rightVisible = True
                rightScore = 1
                rightY = i
                rightX = j
                while rightX < rowLength - 1 and rightVisible:
                    rightX += 1
                    if height <= grid[rightY][rightX]:
                        rightVisible = False
                    else:
                        rightScore += 1
                
                if upVisible or downVisible or leftVisible or rightVisible:
                    # tree is visible
                    visibleTreeCount += 1
    print(visibleTreeCount)
    SolvePart2(grid)        
    return

if __name__ == "__main__":
    main()