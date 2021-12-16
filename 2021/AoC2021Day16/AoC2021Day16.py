#Parse input
input = [line.strip() for line in open("../Inputs/day16.ex", "r")]

class Literal():
    def __init__(self, raw, startingBit):
        self._initialStartingBit = startingBit
        self._helpIndex = startingBit
        self.RawData = raw
        self.Version = int(raw[0:3], 2)
        self._helpIndex += 3
        self.PacketID = int(raw[3:6], 2)
        self._helpIndex += 3
        self.LiteralValue = self.parseLiteral(raw)

    def parseLiteral(self, packet):
        keepReading = True
        bitRepresentation = ""
        while keepReading:
            if packet[self._helpIndex] != "1":
                keepReading = False
            self._helpIndex += 1
            bitRepresentation += packet[self._helpIndex: self._helpIndex + 4]
            self._helpIndex += 4
        self._helpIndex += (self._helpIndex - self._initialStartingBit) % 4
        return int(bitRepresentation, 2)

    def getEndBitPosition(self):
        return (self._helpIndex + self._helpIndex % 4)

    def getVersionCount(self):
        return self.Version


class Operator():
    def __init__(self, raw, startingBit):
        self._helpIndex = startingBit
        self.RawData = raw
        self.Version = int(raw[self._helpIndex:self._helpIndex + 3], 2)
        self._helpIndex += 3
        self.PacketID = int(raw[self._helpIndex:self._helpIndex + 6], 2)
        self._helpIndex += 3
        self.LengthTypeID = int(raw[self._helpIndex], 2)
        self._helpIndex += 1
        self.BitLength = 1e9
        self.PacketLength = 1e9
        if self.LengthTypeID == 0:
            self.L = int(raw[self._helpIndex:self._helpIndex + 15], 2)
            self._helpIndex += 15
            self.BitLength = self.L
        else:
            self.L = int(raw[self._helpIndex:self._helpIndex + 11], 2)
            self._helpIndex += 11
            self.PacketLength = self.L
        self.ContainingPackets = []
        self.extractPackets()

    def extractPackets(self):
        while self.BitLength > 0 and self.PacketLength > 0:
            if int(self.RawData[self._helpIndex + 3:self._helpIndex + 6], 2) == 4:
                self.ContainingPackets.append(Literal(self.RawData, self._helpIndex))
                self.BitLength -= self.ContainingPackets[-1].getEndBitPosition()
                self._helpIndex = self.ContainingPackets[-1].getEndBitPosition()
            elif int(self.RawData[self._helpIndex + 3:self._helpIndex + 6], 2) != 4:
                self.ContainingPackets.append(Operator(self.RawData, self._helpIndex))
                self._helpIndex = self.ContainingPackets[-1].getEndBitPosition()
                self.PacketLength -= 1

    def getEndBitPosition(self):
        return self._helpIndex

    def getVersionCount(self):
        versionCounter = self.Version
        for packet in self.ContainingPackets:
            versionCounter += packet.getVersionCount()
        return versionCounter

#for bibble in input[0]:
bitString = str(bin(int(input[0], 16))[2:].zfill(len(input[0]) * 4))
print(bitString)

if int(bitString[3:6], 2) != 4:
    packet = Operator(bitString, 0)
else:
    packet = Literal(bitString, 0)

print(str(packet.getVersionCount()))