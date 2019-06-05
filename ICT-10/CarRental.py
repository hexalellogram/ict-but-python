class CarRental:
    def __init__(self):
        self.make = input("Please enter the make of the car: ")
        self.model = input("Please enter the model of the car: ")
        self.plate = input("Please enter the license plate for this car: ")

    def generate_code(self):
        letters = self.plate[0:3]
        sum = 0
        for c in letters:
            sum += ord(c)
        sum += int(self.plate[4:7])
        rem = sum % 26
        val = rem + 65
        character = chr(val)
        code = str(character) + str(sum)
        return code


car = CarRental()
print()
print("Results:")
print("Make: " + car.make)
print("Model: " + car.model)
print("Rental Code for above license plate: " + str(car.generate_code()))
