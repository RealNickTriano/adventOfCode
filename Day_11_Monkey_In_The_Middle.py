
from functools import reduce


def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_11_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   

def DetermineOperation(op, worryLevel):
    symbol = op[0]
    number = op[1]
    if op[1] == 'old':
        number = worryLevel
    else:
        number = int(op[1])
        
    if symbol == '*':
        return worryLevel * number, number, 'multiplied'
    elif symbol == '+':
        return worryLevel + number, number, 'added'
    
    return
def SolvePart2(cycleStates):
    
    return

def main():
    data = readInput()
    printList(data)
    
    monkeys = []
    startingItems = []
    operations = []
    tests = []
    truths = []
    falses = []
    for line in data:
        if line[0:6] == 'Monkey':
            monkeys.append(int(line[7]))
        elif line[2:10] == 'Starting':
            splitLine = line[18:].split(', ')
            startingItems.append(list(map(lambda x: int(x), splitLine)))
        elif line[2:11] == 'Operation':
            operation = line[23:]
            operations.append(operation)
        elif line[2:6] == 'Test':
            test = line.split(' ')
            tests.append(int(test[-1]))
        elif line[4:11] == 'If true':
            test = line.split(' ')
            truths.append(int(test[-1]))
        elif line[4:12] == 'If false':
            test = line.split(' ')
            falses.append(int(test[-1]))
            
    print('Monkeys:', monkeys)
    print('Starting Items:', startingItems)
    print('Operations:', operations)
    print('Tests:', tests)
    print('If True:', truths)
    print('If False:', falses)
    
    monkeyInspectionCount = [0 for i in range(len(monkeys))]
    limit = reduce(lambda a, b: a * b, tests)
    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            print('Monkey {}:'.format(i))
            for j, item in enumerate(startingItems[i]):
                worryLevel = startingItems[i][j]
                if worryLevel > limit:
                    worryLevel = worryLevel % limit
                print('\tMonkey inspects an item with a worry level of {}.'.format(worryLevel))
                
                op = operations[i].split(' ')
                worryLevel, number, opString = DetermineOperation(op, worryLevel)
                print('\t\tWorry level is {} by {} to {}.'.format(opString, number, worryLevel))
                
                """ 
                PART 1:
                worryLevel = worryLevel // 3
                print('\t\tMonkey gets bored with item. Worry level is divided by 3 to {}.'.format(worryLevel)) """
                
                
                if worryLevel % tests[i] == 0:
                    print('\t\tCurrent worry level is divisible by {}.'.format(tests[i]))
                    print('\t\tItem with worry level {} is thrown to monkey {}.'.format(worryLevel, truths[i]))
                    startingItems[truths[i]].append(worryLevel)
                else:
                    print('\t\tCurrent worry level is not divisible by {}.'.format(tests[i]))
                    print('\t\tItem with worry level {} is thrown to monkey {}.'.format(worryLevel, falses[i]))
                    startingItems[falses[i]].append(worryLevel)
                #worryLevel = worryLevel % tests[i]
                monkeyInspectionCount[i] += 1
            startingItems[i] = []
                    
    for k, m in enumerate(monkeyInspectionCount):
        print('Monkey {} inspected items {} times.'.format(k, m))
    
    max1 = max(monkeyInspectionCount)
    monkeyInspectionCount.remove(max1)
    max2 = max(monkeyInspectionCount)
    monkeyBusniness = max1 * max2
    print('Level of monkey business after 20 rounds of stuff-slinging simian shenanigans: {}'.format(monkeyBusniness))  
    return

if __name__ == "__main__":
    main()