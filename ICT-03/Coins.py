class Coins:
    def solveCoins(self):
        print(str(self) + " cents =>")
        quarters = self // 25
        print ("Quarters: " + str(quarters))
        rem = self % 25
        dimes = rem // 10
        print("Dimes: " + str(dimes))
        rem = rem % 10
        nickels = rem // 5
        print("Nickels: " + str(nickels))
        rem = rem % 5
        pennies = rem
        print("Pennies: " + str(pennies))
        print("\n")

    solveCoins(35)
    solveCoins(41)
    solveCoins(94)
    solveCoins(59)
    solveCoins(19)
