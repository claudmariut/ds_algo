class LogicGate:
    """Represent Logic Gates. Performs Inputs and Outputs."""
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        return self.performGateLogic()


class BinaryGate(LogicGate):  # Child class. IS-A Relationship
    """Subclass representing two inputs gates."""
    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input(f"Enter Pin A input for gate {self.getLabel()}: "))
        else:
            return self.pinA

    def getPinB(self):
        if self.pinB == None:
            return int(input(f"Enter Pin B input for gate {self.getLabel()}: "))
        else:
            return self.pinB

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source.fromgate.performGateLogic()  # Source is the connector object.
        else:
            if self.pinB == None:
                self.pinB = source.fromgate.performGateLogic() # Source is the connector object.
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    """Subclass representing single input gates."""
    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input(f"Enter Pin input for gate {self.label}: "))
        else:
            return self.pin

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source.fromgate.performGateLogic()  # Source is the output object.
        else:
            raise RuntimeError("Error: NO EMPTY PIN")


class AndGate(BinaryGate):
    """Subclass of Binary Gates that perform the logic."""
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """Subclass of Binary Gates that performs the logic."""
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):
    """Subclass of binary gate."""
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b= self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class NorGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 1
        else:
            return 0


class Xor(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a != b:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    """Subclass of Unary Gate to perform logic."""
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        pin = self.getPin()
        if pin == 1:
            return 0
        else:
            return 1


class Connector:  # HAS-A Relationship.

    def __init__(self, fgate, tgate):  # Instances as parameters.
        self.fromgate = fgate  # Aggregation (vs. Composition)
        self.togate = tgate  # Independent and unidirectional attribute.

        tgate.setNextPin(self)  # If the Pin input is empty it is attributed
        # to the connector object.

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


g1 = AndGate("G1")
g2 = OrGate("G2")
g3 = AndGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
C3 = Connector(g3, g4)
print(g4.getOutput())
