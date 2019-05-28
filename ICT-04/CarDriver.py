import Car as car

auto = car.Car(15)
print("New car odometer reading: " + str(auto.getCurrentMileage()))
auto.fillUp(150, 8)
print("Miles per gallon: " + str(auto.calculateMPG()))
auto.resetMPG()
auto.fillUp(350, 10)
auto.fillUp(450, 20)
print("Miles per gallon: " + str(auto.calculateMPG()))
auto.resetMPG()
auto.fillUp(603, 25.5)
print("Miles per gallon: " + str(auto.calculateMPG()))
