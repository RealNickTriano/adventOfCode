
def printList(myList):
    for item in myList:
        print(item)
    return

def readInput():
    with open('Day_15_input.txt', 'r') as f:
        read_data = f.read()
        
    return read_data.split('\n')   

def SolvePart2(sensors, beacons):
    rowToExamine = 4000000
    mySet = set()
    
    signal = (0, 0)
    for level in range(rowToExamine + 1):
        print(level)
        mySet.clear()
        for j, item in enumerate(sensors):
            myRange = item[2]
            difference = abs(level - item[1])
            #print('Difference:', difference)
            if difference > myRange:
                # cannot reach row
                #print("Can't Reach row")
                continue
            elif difference == myRange:
                # item[1] beacon cannot be
                mySet.add((item[0], level))
            elif difference < myRange:
                distLeft = myRange - difference
                for q in range(distLeft + 1):
                    mySet.add((item[0] + q, level))
                    #print('Sensor:', item, 'Adding:', (item[0] + q, rowToExamine), (item[0] - q, rowToExamine))
                    mySet.add((item[0] - q, level))
        """ for beacon in beacons:
            if beacon in mySet:
                mySet.remove(beacon) """
        #print(sorted(list(map(lambda x: x[0], mySet))))
        for k in range(3000000, rowToExamine + 1):
            if not k in list(map(lambda x: x[0], mySet)):
                print('Found Signal X, Y Pos:', k, level)
                signal = (k, level)
        """ if level == 10:
            print(len(mySet))
            print(sorted(mySet))
    print(sorted(mySet)) """
    print(signal)
    return 1
    
def main():
    data = readInput()
    printList(data)
    
    sensors = []
    beacons = []
    
    for item in data:
        print(item.split(' '))
        sensor_y_coord = int(item.split(' ')[3][2:-1])
        sensor_x_coord = int(item.split(' ')[2][2:-1])
        print('Sensor:', sensor_x_coord, sensor_y_coord)
        sensors.append((sensor_x_coord, sensor_y_coord))
        beacon_y_coord = int(item.split(' ')[-1][2:])
        beacon_x_coord = int(item.split(' ')[-2][2:-1])
        print('Beacon:', beacon_x_coord, beacon_y_coord)
        beacons.append((beacon_x_coord, beacon_y_coord))
    print(sensors)
    print(beacons)
    # Manhatten distance x_diff + y_diff = 
    # distance to beacon from sensor
    
    for i, entry in enumerate(sensors):
        sensor = sensors[i]
        beacon = beacons[i]
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        print(distance)
        sensors[i] = (sensor[0], sensor[1], distance)
    print(sensors)
    
    rowToExamine = 10
    noBeaconPosSet = set()
    for j, item in enumerate(sensors):
        myRange = item[2]
        difference = abs(rowToExamine - item[1])
        #print('Difference:', difference)
        if difference > myRange:
            # cannot reach row
            #print("Can't Reach row")
            continue
        elif difference == myRange:
            # item[1] beacon cannot be
            noBeaconPosSet.add((item[0], rowToExamine))
        elif difference < myRange:
            distLeft = myRange - difference
            for q in range(distLeft + 1):
                noBeaconPosSet.add((item[0] + q, rowToExamine))
                #print('Sensor:', item, 'Adding:', (item[0] + q, rowToExamine), (item[0] - q, rowToExamine))
                noBeaconPosSet.add((item[0] - q, rowToExamine))
    for beacon in beacons:
        if beacon in noBeaconPosSet:
            noBeaconPosSet.remove(beacon)
    print(sorted(noBeaconPosSet))
    print(len(noBeaconPosSet))
    
    SolvePart2(sensors, beacons)
    return

if __name__ == "__main__":
    main()