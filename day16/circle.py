import math
class Circle:
    def __init__(self,radius):
        self._radius=radius
    def get_radius(self):
        return self._radius
    def set_radius(self,new_radius):
        if new_radius>=0:
            self._radius=new_radius
        else:
            print("Radius cannot be negative")
    def calculate_area(self):
        area=math.pi*(self._radius)**2
        return area
example=Circle(7)
print(example.calculate_area())
print(example.get_radius)
example.set_radius(4)
print(example.calculate_area())