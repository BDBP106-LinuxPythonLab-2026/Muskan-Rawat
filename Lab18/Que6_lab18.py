# to calculate the area of triangle using formula.

import math
def area_of_triangle(a,b,c):
    s = (a + b + c)/ 2
    form = s * (s - a) * (s - b) * (s - c)
    math.sqrt(form)
    return math.sqrt(form)

a=area_of_triangle(7,9,8)
print(a)

