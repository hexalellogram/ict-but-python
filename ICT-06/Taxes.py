class Taxes:
    def __init__(self, payRate, hours):
        self.__myFederalRate__ = 0.154
        self.__myFICARate__ = 0.0775
        self.__myStateRate__ = 0.04
        self.__myPayRate__ = float(payRate)
        self.__myHours__ = float(hours)

    def calcGross(self):
        return self.__myHours__ * self.__myPayRate__

    def calcFederal(self):
        return self.calcGross() * self.__myFederalRate__

    def calcFICA(self):
        return self.calcGross() * self.__myFICARate__

    def calcState(self):
        return self.calcGross() * self.__myStateRate__

    def getHours(self):
        return self.__myHours__

    def getPayRate(self):
        return self.__myPayRate__

    def calcTotalTax(self):
        return self.calcFederal() + self.calcFICA() + self.calcState()

tax = Taxes(12.35, 30.0)
print("Hours Worked: " + str(tax.getHours()))
print("Hourly Rate: " + str(tax.getPayRate()))
print("Gross Pay: " + str(tax.calcGross()))
print("Federal Tax 915.4%): " + str(tax.calcFederal()))
print("FICA Tax (7.75%): " + str(tax.calcFICA()))
print("State Tax (4.0%): " + str(tax.calcState()))
print("Net Pay: " + str(tax.calcGross() - tax.calcTotalTax()))