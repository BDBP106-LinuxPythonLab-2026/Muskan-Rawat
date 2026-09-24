import cmath

a=float(input("Enter a digit: "))
b=float(input("Enter a digit: "))
c=float(input("Enter a digit: "))

x = (b**2) - (4*a*c)
cmath.sqrt(x)
print("Root= ", -b + (cmath.sqrt(x))/(2*a))
print("Root= ", -b - (cmath.sqrt(x))/(2*a))