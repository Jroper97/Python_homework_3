from math import pi

def area():
    response = input("What is the length: ")
    response2 = input("What is your width: ")
    area = int(response) * int(response2)
    return area
print(area())

def circumference():
    response = input("What is the radius: ")
    circumference = 2 * pi * int(response)
    return circumference
print(circumference())