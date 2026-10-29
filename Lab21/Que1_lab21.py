#convert Celsius to Fahrenheit without using lambda.

def Func_feh(C):
    cel_flo=float(C)
    fehrenheit= (cel_flo * 1.8) + 32
    return round(fehrenheit)

temp=input('enter a temp:')
temprature=list(map(Func_feh, temp))
print(temprature)