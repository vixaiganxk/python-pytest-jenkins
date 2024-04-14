import math
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        area_of_circle = math.pi * (self.radius ** 2)
        return area_of_circle
    
    def perimeter(self):
        perimeter_of_circle = 2 * math.pi * self.radius
        return perimeter_of_circle


if __name__ == "__main__":
    circle = Circle(5)
    print(f"Area of a circle: {circle.area()}")
    print(f"Perimeter of a circle: {circle.perimeter()}")

