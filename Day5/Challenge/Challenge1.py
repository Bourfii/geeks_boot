import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    @property
    def diametre(self):
        return self.radius * 2
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    def __str__(self):
        return f"The circle with the raduis : {self.radius} , diametre : {self.diametre:.2f} , area : {self.area:.2f}"
    def __add__(self,other):
        return Circle(self.radius + other.radius)
    def __eq__(self,other):
        return self.radius == other.radius
    def __lt__(self,other):
        return self.radius < other.radius

C1 = Circle(3)
C2 = Circle(2)
C3 = Circle(1)
print(C1)
print(C2)
print(C3)
circles=[C1,C2,C3]
sort_circle = sorted(circles)
print("Sorted circles : ")
for C in sort_circle:
    print(C)
C4 = C1 + C2
print(f"The new raduis of the new circle is : \n{C4}")
print("The comparaison :")
if C1 < C2 :
    print(f"The circle 1 : {C1.radius} < The circle 2 : {C2.radius}")
elif C1 == C2 :
    print(f"The circle 1 : {C1.radius} == The circle 2 :{C2.radius}")
elif C1 > C2:
    print(f"The circle 1 : {C1.radius} > The circle 2 : {C2.radius}")     
    
    