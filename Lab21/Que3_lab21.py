#convert a tuple of angles into a list of tuples with each tuple containing the sine and cosine of an angle.

import math

angle=(30,90,45)
def f(angle):
    a=math.sin(math.radians(angle))
    b=math.cos(math.radians(angle))
    return (a,b)


m=tuple(map(f,angle))
print(m)

#using lambda
o=tuple(map(lambda angle:(math.sin(math.radians(angle)) ,math.cos(math.radians(angle))), angle))
print(o)