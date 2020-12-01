class Coins:
    def __init__(self):
        self.coinUsed = {}
        self.change = None

    def coinDynamic(self, coinValueList, change):
        self.change = change
        minCentChange = {0: 0}
        for cent in range(1, change + 1):
            cointCount = cent
            newCoin = 1
            for coin in [c for c in coinValueList if c <= cent]:
                if 1 + minCentChange[cent - coin] < cointCount:
                    cointCount = 1 + minCentChange[cent - coin]
                    newCoin = coin
            minCentChange[cent] = cointCount
            self.coinUsed[cent] = newCoin
        return minCentChange[change]

    def printCoins(self):
        change = self.change
        print("Coins used:")
        while change > 0:
            thisCoin = self.coinUsed[change]
            print(f"-{thisCoin}")
            change = change - thisCoin

# Notice that we are not using recursion in this particular example. Using
# recursion is not always faster. Dynamic programming in this example allow us
# to solve the problem in linear time.
c = Coins()
print(c.coinDynamic([1, 5, 10, 21, 25], 63))
c.printCoins()

