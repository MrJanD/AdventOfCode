class Object(object):
    def __init__(self, name, motherObject):
        self.Name = name
        self.MotherObject = motherObject
        self.Objects_In_Its_Oribit = []

objectList = [Object("COM", None)]
linesOfFile = open("input").readlines()
for line in linesOfFile:
    orbitDefinition = line.split(")")
    objectList.append(Object(orbitDefinition[1].rstrip(), orbitDefinition[0]))

def getTrailOf(objectName):
    objectTrail = []
    for object in objectList:
        if object.Name != objectName:
            continue
        while object.MotherObject is not None:
            for obj in objectList:
                if obj.Name == object.MotherObject:
                    object = obj
                    objectTrail.append(obj)
                    break
    return objectTrail

def getTotalOrbits(objectList):
    totalOrbits = 0
    for object in objectList:
        while object.MotherObject != None:
            totalOrbits += 1
            for obj in objectList:
                if obj.Name == object.MotherObject:
                    object = obj
                    break
    return totalOrbits

def findShortestTrailOfObjects(objectName1, objectName2):
    trailOfObjectName1 = getTrailOf(objectName1)
    trailOfObjectName2 = getTrailOf(objectName2)
    commonObject = findClosestCommonObject(trailOfObjectName1, trailOfObjectName2)

    swingsOfObject1 = 0
    swingsOfObject2 = 0

    for object1Orbit in trailOfObjectName1:
        if object1Orbit.Name != commonObject.Name:
            swingsOfObject1 += 1
        else:
            break

    for object2Orbit in trailOfObjectName2:
        if object2Orbit.Name != commonObject.Name:
            swingsOfObject2 += 1
        else:
            break

    return swingsOfObject1 + swingsOfObject2

def findClosestCommonObject(trailOfObjectName1, trailOfObjectName2):
    for object1Orbit in trailOfObjectName1:
        for object2Orbit in trailOfObjectName2:
            if object1Orbit.Name == object2Orbit.Name:
                return object1Orbit

print("Total number of orbits: " + str(getTotalOrbits(objectList)))
print("Orbital swings required to reach santa: " + str(findShortestTrailOfObjects("YOU", "SAN")))

