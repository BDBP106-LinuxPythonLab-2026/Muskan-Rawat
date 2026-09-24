x=float(input("Enter first point: "))
y=float(input("Enter second point: "))

if x > 0 and y > 0:
    print("Point lies in the first quadrant")
elif x < 0 and  y > 0:
    print("Point lies in the second quadrant")
elif x < 0 and y < 0:
    print("Point lies in the third quadrant")
elif x > 0 and y < 0:
    print("Point lies in the fourth quadrant")
elif x == 0:
    print("Point lies on the y axis")
elif y==0:
    print("Point lies on the x axis")
else:
    print("point lies at the origin")
