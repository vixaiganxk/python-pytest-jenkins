import pytest
from calculation import Circle
import math

@pytest.mark.parametrize("radius, expected_area", [(1, 1 * math.pi), (2, 4 * math.pi), (5, 25 * math.pi), (15, 2205 * math.pi)])
def test_area(radius, expected_area):
    #instance creation
    circle = Circle(radius)

    #Checking the area matches the expected area
    assert circle.area() == expected_area

#Checking the perimeter
@pytest.mark.parametrize("radius, expected_perimeter", [(1, 2 * math.pi), (5, 10 * math.pi), (55, 110 * math.pi), (250, 500 * math.pi)])
def test_perimeter(radius, expected_perimeter):
    #instance creation
    circle = Circle(radius)

    #checking the perimeter
    assert circle.perimeter() == expected_perimeter
