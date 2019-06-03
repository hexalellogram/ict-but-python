class CheckMail:
    def __init__(self):
        self.dimensions = []
        for i in range(0, 3):
            data = input("Enter a dimension: ")
            self.dimensions.append(data)
        self.weight = input("Enter a weight: ")

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
        return int(self.weight) < 70

    def test_sum_length_girth(self):
        length = int(self.determine_longest())
        others = int(0)
        for i in self.dimensions:
            if i != length:
                others += int(i)
        others *= 2
        return length + others < 100

    def test_package(self):
        if self.test_weight() is False and self.test_sum_length_girth() is False:
            print("Package is too large and too heavy.")
        elif self.test_sum_length_girth() is False:
            print("Package is too large.")
        elif self.test_weight() is False:
            print("Package is too heavy.")
        else:
            print("Package is acceptable.")


package = CheckMail()
package.test_package()
