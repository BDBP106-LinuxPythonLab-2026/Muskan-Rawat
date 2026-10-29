# sum of all the values in dictionary.

D=dict([('1', '1'), ('2', '2'), ('3', '6'), ('4', '10'), ('5', '5')])
a=0
values=D.values()
for i in values:
    if i > 0:
        a+=i
print(a)