"""
The problem is valid if amount < smallJug or < largeJug and if amount is
divisible by the greatest common denominator of smallJug and largeJug.
"""

class Jug:
    def __init__(self, smallJug, largeJug, amount):
        self.smallJug = 0
        self.largeJug = 0
        self.amount = amount
        self.smallCapacity = smallJug
        self.largeCapacity = largeJug
        self.gcd()

    def gcd(self):
        """Returns gdc using Euclid's Algorithm"""
        m = self.smallCapacity
        n = self.largeCapacity
        while m % n != 0:
            oldm = m
            oldn = n

            n = oldm % oldn
            m = oldn
        if self.amount % n == 0:
            print("Valid Problem")
        else:
            self.smallCapacity = 0
            self.largeCapacity = 0
            self.amount = 0
            print("Invalid Problem")

    def jug(self):
        """Solve jug problem taking two jugs and final amount on larger."""
        # Base case when large jug equals target amount.
        print(f"Small Jug: {self.smallJug} liters,"
              f" Large Jug: {self.largeJug} liters")
        if self.largeJug == self.amount:
            return

        # If small jug is empty, fill it.
        if self.smallJug == 0:
            self.smallJug = self.smallCapacity
            print(f"Small Jug: {self.smallJug} liters,"
                  f" Large Jug: {self.largeJug} liters")

        # If large jug is completely filled. Dump it.
        if self.largeJug == self.largeCapacity:
            self.largeJug = 0
            print(f"Small Jug: {self.smallJug} liters,"
                  f"Large Jug: {self.largeJug} liters")

        # If small jug is going to exceed large. Pour only available.
        if (self.largeJug + self.smallJug) > self.largeCapacity:
            temp = self.largeCapacity - self.largeJug
            self.largeJug += temp
            self.smallJug -= temp

        # Pour amount from small jug to small.
        else:
            self.largeJug += self.smallJug
            self.smallJug = 0

        # Recursion call.
        self.jug()


j = Jug(3, 5, 4)
j.jug()
