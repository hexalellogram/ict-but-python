import Rectangle as rect

rectA = rect.Rectangle()
print("RectA Perimeter: " + str(rectA.getPerimeter()))
print("RectA Area: " + str(rectA.getArea()))
rectB = rect.Rectangle(0, -80, 400, 160)
print("RectB Perimeter: " + str(rectB.getPerimeter()))
print("RectB Area: " + str(rectB.getArea()))
rectC = rect.Rectangle(100, -100, 20, 300)
print("RectC Perimeter: " + str(rectC.getPerimeter()))
print("RectC Area: " + str(rectC.getArea()))