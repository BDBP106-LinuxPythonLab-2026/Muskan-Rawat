# to find out if what type of triangle it is.

def triangle(a,b,c):
    if a == b == c :
        print(" Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

    return

print(triangle(6,7,8))