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
            coinValueList = [c for c in coinValueList if c <= change]
            self.a += 1
            optimal = max(coinValueList)
            minCoins = 1 + self.recMC(coinValueList, change - optimal)
        return minCoins

# Using the greedy method is much more efficient, but does not resolve the problem
# since we could use 3 "21 coins", for instance... And the program will still
# show 6 coins to change instead of three.
c = Coins()
print(c.recMC([1, 5, 10, 21, 25], 63))
print("Number of functions calls: ", end="")
print(c.a)
