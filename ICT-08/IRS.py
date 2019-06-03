class IRS:
    def __init__(self):
        self.status = input("Enter marital status (1 = single, 2 = married): ")
        self.income = float(input("Enter taxable income: $"))

    def calc_tax(self):
        if self.status == 1:
            return self.calc_single()
        else:
            return self.calc_married()

    def calc_single(self):
        if self.income < 27050:
            return 0.15 * self.income
        elif self.income < 65550:
            return float(4057.50) + 0.275 * (self.income - 27050)
        elif self.income < 136750:
            return float(14645) + 0.305 * (self.income - 65550)
        elif self.income < 297350:
            return float(36361) + 0.355 * (self.income - 136750)
        else:
            return float(93374) + 0.391 * (self.income - 297350)

    def calc_married(self):
        if self.income < 45200:
            return 0.15 * self.income
        elif self.income < 109250:
            return float(6780) + 0.275 * (self.income - 45200)
        elif self.income < 166500:
            return float(24393.75) + 0.305 * (self.income - 109250)
        elif self.income < 297350:
            return float(41855) + 0.355 * (self.income - 166500)
        else:
            return float(88306) + 0.391 * (self.income - 297350)


taxes = IRS()
fed = taxes.calc_tax()
print("Your Federal Tax = " + str(fed))
