N=int(input("Enter a number: "))
while N>0:
    dig=N%10
    N//=10
    print("Individual digit of a number: ", dig)
