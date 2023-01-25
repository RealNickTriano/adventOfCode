import string
import heapq
class Node:
    def __init__(self, row, col, dist, value) -> None:
        self.row = row
        self.col = col
        self.dist = dist
        self.value = value
        
def printList(myList):
    for item in myList:
        print(item)
    return

def printGrid(myList):
    for item in myList:
        print(list(map(lambda x: x.value, item)))
    return

def readInput():
    with open('Day_12_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   
    
def SolvePart2():
    
    return

def heightOf(row, col, grid):
    if grid[row][col] == 'S':
        return 0
    elif grid[row][col] == 'E':
        return 25
    else:
        return string.ascii_lowercase.index(grid[row][col])

def findNeighbors(row, col, grid):
    possibleNeighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    neighbors = []
    for item in possibleNeighbors:
        newRow = row + item[0]
        newCol = col + item[1]
        if ((0 <= newRow < len(grid)) and (0 <= newCol < len(grid[0]))):
            # this node is in bounds
            if heightOf(newRow, newCol, grid) >= heightOf(row, col, grid) - 1:
                # Passes height test
                neighbors.append((newRow, newCol))
    return neighbors

def main():
    data = readInput()
    printList(data)
    
    grid = []
    for i, row in enumerate(data):
        grid.append(list(row))
    printList(grid)
    
    n = len(grid)
    m = len(grid[0])
    start = []
    end = None
    # Find start and end
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'E':
                end = (0, i, j)

    # dijkstra's
    minGoal = 500
    heap = []

    heapq.heappush(heap, end)
    visited = [[False for k in range(len(grid[0]))] for q in range(len(grid))]
    #printList(visited)
    while True:
        currentNode = heapq.heappop(heap)
        if visited[currentNode[1]][currentNode[2]]:
            continue
        visited[currentNode[1]][currentNode[2]] = True
        if currentNode[0] > minGoal:
            break
        print('current node:', currentNode)
        if grid[currentNode[1]][currentNode[2]] == 'a':
            print('Found goal:', currentNode)
            minGoal = currentNode[0]
            break
            
        neighbors = findNeighbors(currentNode[1], currentNode[2], grid)
        print(neighbors)
        for entry in neighbors:
            heapq.heappush(heap, (currentNode[0] + 1, entry[0], entry[1]))
            print('NEIGHBOR:', (currentNode[0] + 1, entry[0], entry[1]))
    print(minGoal)
    return

if __name__ == "__main__":
    main()