
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_7_input.txt', 'r') as f:
        read_data = f.read()
        print(read_data)
        
    return read_data.split('\n')   
      
def SolvePart2(data):

    return

class Node:
    def __init__(self, name, parent = None) -> None:
        self.parent = parent
        self.children = []
        self.name = name
    
    def setChildren(self, children):
        self.children = children
        
    def getChild(self, name):
        print('Children', self.children)
        for child in self.children:
            if isinstance(child, Node):
                if child.name == name:
                    return child
        print('ERROR: CHILD NOT FOUND')
        return -1
    
    def getChildren(self):
        return list(map(lambda x: str(x), self.children))
        
    def printTree(self):
        root = self
        while self.parent is not None:
            root = self.parent
        print(root.name, root.children)

dirValues = []

def FindSumOfDir(dir):
    sum = 0
    for i, item in enumerate(dir.children):
        if isinstance(item, Node):
            sum += FindSumOfDir(item)
        else:
            print('COUNTING...', int(item[0]))
            sum += int(item[0])
    return sum

dirs = []

def ComputeSumForEachDir(root):
    dirs.append(root)
    for i, item in enumerate(root.children):
        if isinstance(item, Node):
            ComputeSumForEachDir(item)
    return

def FileAlreadyMade(currentDir, name):

    for item in currentDir.children:
        if isinstance(item, Node):
            if item.name == name:
                return True
        else:
            if item[1] == name:
                return True
    return False

def main():
    data = readInput()
    printList(data)
    
    currentDir = Node('/')
    parentDir = None
    initialize = True
    files = []
    trackOutput = False
    for i, item in enumerate(data):
        """
        cd = change current dir
        ls = add output to current dir children
        how to track output of ls?
            keep array of output lines
            flush and set children of current dir once u see $
        after all commands, should have tree of nodes
        in the right place, can then traverse to sum totals <= 100000
        """
        if (item[0] == '$' and trackOutput) or (trackOutput and item == data[-1]):
            if item == data[-1]:
                size, name = item.split(' ')
                files.append((size, name))
            currentDir.setChildren(files)
            print('SETTING CHILDREN')
            print(currentDir.name, currentDir.children)
            trackOutput = False
            files = []
            
        if trackOutput:
            if item[0:3] == 'dir':
                print('tracking dir', item[4:])
                if not FileAlreadyMade(currentDir, item[4:]):
                    newNode = Node(item[4:], currentDir)
                    print('New node parent:', newNode.parent.name)
                    files.append(newNode)
            else:
                if not FileAlreadyMade(currentDir, item[4:]):
                    size, name = item.split(' ')
                    files.append((size, name))
                
        if item == '$ ls':
            trackOutput = True
        elif item == '$ cd ..':
            if currentDir.parent != None:
                currentDir = currentDir.parent
                print('Moved back one dir, New Dir:', currentDir.name)
        elif item[0:4] == '$ cd' and not item == '$ cd /':
            dirToMoveTo = item[5:]
            print('Moving to this dir', dirToMoveTo)
            currentDir = currentDir.getChild(dirToMoveTo)
            print('Succesfully moved to this dir:', currentDir.name)
            
    while currentDir.parent is not None:
        currentDir = currentDir.parent
    print(currentDir.name)
    ComputeSumForEachDir(currentDir)  
    printList(dirs)
    values = list(map(lambda x: (FindSumOfDir(x), x.name), dirs))
    printList(values)
    total = 0
    for dir in values:
        if dir[0] < 100000:
            total += dir[0]
    print(total)
    
    #------- Part 2 -------------#
    unusedSpace = 70000000 - values[0][0]
    spaceToFreeUp = 30000000 - unusedSpace
    candidateToDelete = 70000000
    for entry in values:
        if entry[0] >= spaceToFreeUp:
            print(candidateToDelete, entry[0], entry)
            if entry[0] < candidateToDelete:
                candidateToDelete = entry[0]

    print(candidateToDelete)
    return

if __name__ == "__main__":
    main()