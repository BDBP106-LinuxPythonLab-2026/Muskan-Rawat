import math
x1=float(input("Enter a x1:"))
y1=float(input("Enter a y2: "))
x2=float(input("Enter a x2: "))
y2=float(input("Enter a y2: "))

first_point = (x1, y1)
second_point = (x2, y2)

math.dist(first_point, second_point)
print("The distance between two point= ",math.dist(first_point, second_point))