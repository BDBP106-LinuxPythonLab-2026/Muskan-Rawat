# maximum and minimum values of a dictionary.

D=dict([(1, 7), (2, 2), (3, 6), (4, 10), (5, 5)])

maxi=D.get(1)
mini=D.get(1)
val=D.values()
for i in val:
    if i > maxi :
        maxi = i
    elif i < mini :
        mini = i
print(maxi)
print(mini)
