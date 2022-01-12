import math

MAX_SIZE = 10000

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

def square_area(length):
    return length * 2

