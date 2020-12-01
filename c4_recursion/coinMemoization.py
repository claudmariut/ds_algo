
# In this case will use the same approach as we did in the recursion "brute
# force" solution. But will store results for the minimum number of coins in a
# table as we find them.  So if the value is higher or is already in the table
# we found another base case.

class Coins:
    def __init__(self):
        self.a = 0
        self.knownResults = {}

    def recDC(self, coinValueList, change):
        """Return minimum amount of coins."""
        minCoins = change
        if change in coinValueList:
            return 1
        elif change in self.knownResults.keys():
            return self.knownResults[change]
        else:
            for i in [c for c in coinValueList if c <= change]:
                self.a += 1
                numCoins = 1 + self.recDC(coinValueList, change - i)
                if numCoins < minCoins:
                    minCoins = numCoins
                    self.knownResults[change] = minCoins
        return minCoins


# This technique is called memoization. (In computing, memoization or m
# emoisation is an optimization technique used primarily to speed up computer
# programs by storing the results of expensive function calls and returning
# the cached result when the same inputs occur again.
c = Coins()
print(c.recDC([1, 5, 10, 21, 25], 63))
print("Number of functions calls: ", end="")
print(c.a)
