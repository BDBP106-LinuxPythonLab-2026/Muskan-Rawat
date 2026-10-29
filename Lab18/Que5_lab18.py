#remove all duplicate words from a given sentence.

D=dict([('1', 'this'),('2', 'is'), ('3','is'),('4','a'), ('5','a'), ('6','file')])
m=D.values()
a=set(m)
print(a)