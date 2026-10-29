#population growth using exponential growth formula.

import math

def population_growth(initial,rate,time):
    def exponential_growth():

        formula= initial * math.pow((1+rate),time)
        return formula
    return round(exponential_growth())

initial=int(input('enter the initial population: '))
rate=int(input('enter the rate at which the population increased: '))
time=int(input('enter the time: '))
k=population_growth(initial,rate,time)
print("the population after time 't' is equal to",k)



