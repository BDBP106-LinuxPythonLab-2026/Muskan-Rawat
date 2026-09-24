numbr=int(input("Enter a number: "))
sum=0
while numbr>0:
    r=numbr%10 #takes last digit
    sum+=r
    numbr//=10 #removes last digit and does not print in decimal."//" is integer division.
print("sum of two digits of number=",sum)
