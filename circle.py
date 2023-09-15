import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
            return math.pi * (self.radius ** 2)
        
    def perimeter(self):
            return math.pi * self.radius
        
radius = float(input("input the radius"))
circle = Circle(radius)
areaOfCircle = circle.area()
perimeterOfCircle = circle.perimeter()
print("Area of circle is : " , areaOfCircle)
print("Perimeter of circle is : " , perimeterOfCircle)