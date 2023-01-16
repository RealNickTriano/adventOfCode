def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    opponentChoices = []
    myChoices = []
    with open('Day_2_input.txt', 'r') as f:
        read_data = f.read()
        print(read_data)
        counts = read_data.split('\n')
        print(counts)
        for i, item in enumerate(counts):
            choices = item.split(' ')
            print(choices)
            if choices[0] == '':
                continue
            else:
                opponentChoices.append(choices[0])
                myChoices.append(choices[1])
                
    return opponentChoices, myChoices

def SolvePart2():
    # key: opp choice, value: myChoice 
    # 1 Rock, 2 Paper, 3 Scissors
    win = {'A': 2, 'B': 3, 'C': 1}
    draw = {'A': 1, 'B': 2, 'C': 3}
    lose = {'A': 3, 'B': 1, 'C': 2}
    resultValues = {'X': 0, 'Y': 3, 'Z': 6}
    
    opponentChoices, myChoices = readInput()
    
    totalScore = 0
    
    for i, item in enumerate(opponentChoices):
        if myChoices[i] == 'X':
            shapeValue = lose[opponentChoices[i]]
            roundValue = resultValues['X']
        elif myChoices[i] == 'Y':
            shapeValue = draw[opponentChoices[i]]
            roundValue = resultValues['Y']
        elif myChoices[i] == 'Z':
            shapeValue = win[opponentChoices[i]]
            roundValue = resultValues['Z']
        
        totalScore += shapeValue + roundValue
    
    print(totalScore)
    
    return

def main():
    # A: Rock
    # B: Paper
    # C: Scissors
    # X: Rock
    # Y: Paper
    # Z: Scissors
    myDict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
              'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
    resultsDict = {('A','Y'): 8, ('A', 'X'): 4, ('A', 'Z'): 3,
                   ('B', 'Y'): 5, ('B', 'X'): 1, ('B', 'Z'): 9,
                   ('C', 'Y'): 2, ('C', 'X'): 7, ('C', 'Z'): 6,}
    
    opponentChoices, myChoices = readInput()
    
    totalScore = 0
    for i, item in enumerate(opponentChoices):
        roundScore = resultsDict[(opponentChoices[i], myChoices[i])]
        totalScore += roundScore
        
    print(opponentChoices)
    print(myChoices)
    print(totalScore)
    SolvePart2()
    return
    
if __name__ == "__main__":
    main()