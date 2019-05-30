class GroceryList:
    def __init__(self):
        self.itemList = ["", "", "", "", ""]
        for i, name in enumerate(self.itemList):
            self.itemList[i] = input("Enter Item #" + str(i+1) + ": ")

    def output_prices(self):
        print("{:>10}{:>10}{:>10}".format("Item:", "Cost:", "Total:"))
        total = 0
        for i, name in enumerate(self.itemList):
            total += float(self.itemList[i])
            print("{:>10}{:>10.2f}{:>10.2f}".format("#" + str(i+1), float(self.itemList[i]), float(total)))


listOfItems = GroceryList()
listOfItems.output_prices()
