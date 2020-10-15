addition = []

class FullAdder8Bit:
    """Represent 8 bit circuit full adder."""
    def __init__(self, n):
        self.label = n
        self.inA = None
        self.inB = None
        self.sum = None
        self.carryOut = None

    def getInA(self):
        self.inA = int(input(f"Enter pin A for {self.label}: "))
        return self.inA

    def getInB(self):
        self.inB = int(input(f"Enter pin B for {self.label}: "))
        return self.inB

    def getOutput(self):
        self.performOutput()
        addition.append(self.carryOut)
        addition.reverse()
        for number in addition:
            print(number, end='')
        print("\n")


class HalfAdder(FullAdder8Bit):
    """Represent Half Adder circuit"""
    def __init__(self, n):
        super().__init__(n)

    def __str__(self):
        return f"{self.label} is an instance of Half Adder"

    def performOutput(self):
        a = self.getInA()
        b = self.getInB()

        self.sum = self.performXorGate()
        self.carryOut = self.performAndGate()

        addition.append(self.sum)

    def getCarryOut(self):
        if self.carryOut == None:
            self.performOutput()
        else:
            return self.carryOut

    def performAndGate(self):
        if self.inA == 1 and self.inB == 1:
            return 1
        else:
            return 0

    def performXorGate(self):
        if self.inA != self.inB:
            return 1
        else:
            return 0


class FullAdder(FullAdder8Bit):
    """Represent a full adder circuit"""
    def __init__(self, n):
        super().__init__(n)
        self.carryIn = None

    def __str__(self):
        return f"{self.label} is an instance of Full Adder"

    def getCarryIn(self):
        self.carryIn = int(input(f"Enter C_in for {self.label}: "))
        return self.carryIn

    def performOutput(self):
        a = self.getInA()
        b = self.getInB()
        if self.carryIn == None:
            self.carryIn = self.getCarryIn()
        else:
            self.carryIn.getCarryOut()
            self.carryIn = self.carryIn.getCarryOut()
        self.sum = self.performXorGate(self.carryIn, self.performXorGate(a, b))
        self.carryOut = \
            self.performOrGate(self.performAndGate(a, b),
                               self.performAndGate(self.carryIn,
                                                   self.performXorGate(a, b)))
        addition.append(self.sum)

    def getCarryOut(self):
        if self.carryOut == None:
            self.performOutput()
        else:
            return self.carryOut

    def performAndGate(self, pin1, pin2):
        if pin1 == 1 and pin2 == 1:
            return 1
        else:
            return 0

    def performXorGate(self, pin1, pin2):
        if pin1 != pin2:
            return 1
        else:
            return 0

    def performOrGate(self, pin1, pin2):
        if pin1 == 1 or pin2 == 1:
            return 1
        else:
            return 0

    def setNextCin(self, source):
        """If the pin is empty, it attributed to the source object."""
        if self.carryIn == None:
            self.carryIn = source.getFrom()


class Connector:
    """Connects Half Adder to Full Adder to create 8-bit full-adder."""
    def __init__(self, fadder, tadder):
        self.fromAdder = fadder
        self.toAdder = tadder

        tadder.setNextCin(self)

    def getFrom(self):
        return self.fromAdder

    def getTo(self):
        return self.toAdder


# 8-bit Full Adder. Binary Numbers Adder.
h1 = HalfAdder("S1")
f2 = FullAdder("S2")
f3 = FullAdder("S3")
f4 = FullAdder("S4")
f5 = FullAdder("S5")
f6 = FullAdder("S6")
f7 = FullAdder("S7")
f8 = FullAdder("S8")
c1 = Connector(h1, f2)
c2 = Connector(f2, f3)
c3 = Connector(f3, f4)
c4 = Connector(f4, f5)
c5 = Connector(f5, f6)
c6 = Connector(f6, f7)
c7 = Connector(f7, f8)
f8.getOutput()

