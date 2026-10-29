#list using list comprehension method.
a=[i for i in range(0,51)]
print(a)

#slicing with positive step.

print(a[1:5], a[3:20:2], a[::2], a[::], a[10::2], a[1:1:1], a[:0:], a[-7::1], a[-6:], a[-10:-4])

#slicing with negative step.

print(a[::-1], a[::-3], a[:1:-2], a[-1:-1:-1],a[:-5:-1],a[:0:-1],a[:-5:-1], a[:0:-1], a[:-1:-1],a[0:-5:-1], a[-1:5:-1], a[2:2:-1],a[2:1:-1],a[0:-5])

#create a list of even numbers from a using list slicing method.
print("List of even numbers: ", a[0:50:2])

#new list of first 10 numbers and then even numbers from 35 to 50.
print(a[0:10:]+a[34:50:2]) #to combine two separate list '+' can be used.