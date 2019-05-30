class CheckMail:
    def __init__(self):
        self.dimensions = []
        for i in range(0,2):
            data = input("Enter a dimension:")
            self.dimensions.append(data)
        self.weight = input("Enter a weight:")

    def determine_longest(self):
        if self.dimensions[0] < self.dimensions[1]:
            temp = self.dimensions[0]
            self.dimensions[0] = self.dimensions[1]
            self.dimensions[1] = temp
        if self.dimensions[0] < self.dimensions[2]:
            temp = self.dimensions[0]
            self.dimensions[0] = self.dimensions[2]
            self.dimensions[2] = temp
        return self.dimensions[0]

    def test_weight(self):
        return int(self.weight) > 70

package = CheckMail()
print("Is the package within weight  bounds?" + str(package.test_weight()))