import ast
import functools
      
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_13_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   


   
def SolvePart2():
    data = readInput()
    printList(data)
    
    newData = [i for i in data if not i == '']
    dataInListForm = list(map(lambda x: ast.literal_eval(x), newData))
    dataInListForm.append([[2]])
    dataInListForm.append([[6]])
    print(dataInListForm)
    sortedData = sorted(dataInListForm, key=functools.cmp_to_key(compare))
    print((sortedData.index([[2]]) + 1) * (sortedData.index([[6]]) + 1))
    print()
    
    return

def compare(left, right):
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    
    if isinstance(left, int) and isinstance(right, int):
        print('Compare {} vs {}'.format(left, right))
        if left < right:
            # return 1 # Part 1
            return -1 # Part 2
        if left == right:
            return 0
        # return -1 # Part 1
        return 1 # Part 2
    
    if isinstance(left, list) and isinstance(right, list):
        i = 0
        print('Compare {} vs {}'.format(left, right))
        print('LENGTHS:', len(left), len(right))
        while i < len(left) and i < len(right):
            result = compare(left[i], right[i])
            if result == 1:
                return 1
            if result == -1:
                return -1
            
            i += 1
        
        if i == len(left):
            if i == len(left) and i == len(right):
                return 0
            # return 1 # Part 1
            return -1 # Part 2
        
        # return -1 # Part 1
        return 1 # Part 2
    
def main():
    data = readInput()
    printList(data)

    newData = [i for i in data if not i == '']
    dataInListForm = list(map(lambda x: ast.literal_eval(x), newData))
    
    pairs = []
    for i in range(0, len(dataInListForm), 2):
        pairs.append((dataInListForm[i], dataInListForm[i + 1])) 
    
    print()    
    printList(pairs)
    
    rightPairsIndex = []
    for j, pair in enumerate(pairs):
        left = pair[0]
        right = pair[1]
        print(left, right)
        if compare(left, right) == 1:
            rightPairsIndex.append(j + 1)
    
    print(rightPairsIndex)        
    print(functools.reduce(lambda a, b: a + b, rightPairsIndex))  
    SolvePart2()     
    return

if __name__ == "__main__":
    main()