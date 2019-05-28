class PiggyBank:
    def __init__(self, quarters=None, dimes=None, nickels=None, pennies=None):
        if quarters is not None:
            self.__myQuarters__ = quarters
        else:
            self.__myQuarters__ = 0
        if dimes is not None:
            self.__myDimes__ = dimes
        else:
            self.__myDimes__ = 0
        if nickels is not None:
            self.__myNickels__ = nickels
        else:
            self.__myNickels__ = 0
        if pennies is not None:
            self.__myPennies__ = pennies
        else:
            self.__myPennies__ = 0

    def getpennies(self):
        return self.__myPennies__

    def getnickels(self):
        return self.__myNickels__

    def getdimes(self):
        return self.__myDimes__

    def getquarters(self):
        return self.__myQuarters__

    def getvalue(self):
        return 0.25*self.__myQuarters__ + 0.10*self.__myDimes__ + 0.05*self.__myNickels__ + 0.01*self.__myPennies__

    def addquarters(self, quarters):
        self.__myQuarters__ += int(quarters)

    def adddimes(self, dimes):
        self.__myDimes__ += int(dimes)

    def addnickels(self, nickels):
        self.__myNickels__ += int(nickels)

    def addpennies(self, pennies):
        self.__myPennies__ += int(pennies)
