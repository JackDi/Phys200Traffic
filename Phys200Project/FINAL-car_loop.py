def Porj(NumberCar, NumberStep):
    numStep = NumberStep #number of steps, change to user input
    numCar = NumberCar
    density = []
    lenRoad = 100 #number of spaces on road
    curRoad = [] #the current road, a list of car objects
    c = 0
    n = 0
    import copy
    q = 0
    initalPos = []
    while q < numCar:
        rad = random.randint(0, lenRoad)
        if rad not in initalPos:
            initalPos.append(rad)
            q += 1
    for iPos in initalPos:
        curRoad.append(Car(iPos, 5))
    while n < numStep: #This will visualize the current road and make a new one
        newRoad = [] #road to be made, will replaces curRoad
        posLis = []
        namLis = []
        index = 1
        firstPos = 101
        lastPos = -1
        for b in curRoad: #makes list for visualization
            posLis.append(b.pos)
            if(b.pos < firstPos):
                firstPos = b.pos
            if(b.pos > lastPos):
                lastPos = b.pos
            namLis.append(index)
            index += 1
        density.append( float(numCar)/float(lastPos + 1. - firstPos) ) #density of step
        visualize(namLis, posLis) #Visualizes current road
        street = [0]*(lenRoad+1)
        for a in curRoad:
            street[a.pos] = 1
        for car in curRoad:
            newCar = copy.copy(car)
            newCar.pos = car.move_car(street)
            newRoad.append(newCar) #adds the new car to the new road
        curRoad = newRoad
        #time.sleep(1)
        n +=1
    
    return density
