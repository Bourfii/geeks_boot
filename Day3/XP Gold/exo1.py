import math
class Circle:
    def __init__(self,raduis=1.0):
        self.raduis = raduis
    def perimeter(self):
        return 2 * math.pi * self.raduis    
    def area(self):
        return math.pi * (self.raduis ** 2)
    def definition(self):
        print("A circle is a shape with all points the same distance from its center.")

c = Circle(8.3)
print("Perimeter:", c.perimeter())
print("Area:", c.area())
c.definition()
