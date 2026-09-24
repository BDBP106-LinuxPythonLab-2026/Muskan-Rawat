length1=int(input("Enter the length of one side: "))
length2=int(input("Enter the length of second side: "))
length3=int(input("Enter the length of third side: "))
if length1==length2==length3:
    print("Equilateral Triangle")
elif length1 == length2:
    print("Isosceles Triangle")
elif length2 == length3:
    print("Isosceles Triangle")
elif length3 == length1:
    print("isosceles Triangle")
else:
    print("Scalene Triangle")