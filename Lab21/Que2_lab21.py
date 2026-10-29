# convert Celsius to Fahrenheit using lambda

Celsius_temp=[0,10,25,67]
temp=list(map(lambda C: round((C * 1.8)+32),Celsius_temp))
print(temp)