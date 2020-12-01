class Coins:
    def __init__(self):
        self.a = 0

    def recMC(self, coinValueList, change):
        """Return minimum amount of coins."""
        minCoins = change
        if change in coinValueList:
            return 1
        else:
            # We create a new list that only contains coins less than or  equal
            # to the change.
            for i in [c for c in coinValueList if c <= change]:
                self.a += 1
                numCoins = 1 + self.recMC(coinValueList, change - i)
                if numCoins < minCoins:
                    minCoins = numCoins
        return minCoins


# Not very good algorithm. Is like brute force, because it explores every
# single branch until change is equal to some of the coins in list.
c = Coins()
print(c.recMC([1, 5, 10, 21, 25], 63))
print("Number of functions calls: ", end="")
print(c.a)


