#sum of all the elements in a list
from functools import reduce

List=[1,2,3,4,5,6]

Sum=reduce(lambda x,y: x + y, List)
print(sum)
