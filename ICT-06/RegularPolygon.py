import math as math


class RegularPolygon:
    def __init__(self, num_sides=None, side_length=None):
        if num_sides is not None:
            self.myNumSides = num_sides
        else:
            self.myNumSides = 3
        if side_length is not None:
            self.mySideLength = side_length
        else:
            self.mySideLength = 1.0

    def vertex_angle(self):
        return ((self.myNumSides - 2)/self.myNumSides) * 180

    def perimeter(self):
        return self.myNumSides * self.mySideLength

    def radius_inscribed(self):
        return 0.5 * self.mySideLength * 1/math.tan(math.pi/self.myNumSides)

    def radius_circumscribed(self):
        return 0.5 * self.mySideLength * 1/math.sin(math.pi/self.myNumSides)

    def area(self):
        return 0.5 * self.myNumSides * self.radius_circumscribed()**2 * math.sin(2 * math.pi / self.myNumSides)


print("Square:")
shape = RegularPolygon(4, 10)
print("Number of sides: " + str(shape.myNumSides))
print("Side length: " + str(shape.mySideLength))
print("Vertex Angle: " + str(shape.vertex_angle()))
print("Inscribed circle radius: " + str(shape.radius_inscribed()))
print("Circumscribed circle radius: " + str(shape.radius_circumscribed()))
print("Perimeter: " + str(shape.perimeter()))
print("Area: " + str(shape.area()))
print("\n")

print("Octagon:")
shape = RegularPolygon(8, 5.75)
print("Number of sides: " + str(shape.myNumSides))
print("Side length: " + str(shape.mySideLength))
print("Vertex Angle: " + str(shape.vertex_angle()))
print("Inscribed circle radius: " + str(shape.radius_inscribed()))
print("Circumscribed circle radius: " + str(shape.radius_circumscribed()))
print("Perimeter: " + str(shape.perimeter()))
print("Area: " + str(shape.area()))
print("\n")

print("Enneadecagon:")
shape = RegularPolygon(19, 2)
print("Number of sides: " + str(shape.myNumSides))
print("Side length: " + str(shape.mySideLength))
print("Vertex Angle: " + str(shape.vertex_angle()))
print("Inscribed circle radius: " + str(shape.radius_inscribed()))
print("Circumscribed circle radius: " + str(shape.radius_circumscribed()))
print("Perimeter: " + str(shape.perimeter()))
print("Area: " + str(shape.area()))
print("\n")

print("Enneacontakaihenagon:")
shape = RegularPolygon(91, 0.5)
print("Number of sides: " + str(shape.myNumSides))
print("Side length: " + str(shape.mySideLength))
print("Vertex Angle: " + str(shape.vertex_angle()))
print("Inscribed circle radius: " + str(shape.radius_inscribed()))
print("Circumscribed circle radius: " + str(shape.radius_circumscribed()))
print("Perimeter: " + str(shape.perimeter()))
print("Area: " + str(shape.area()))
print("\n")
