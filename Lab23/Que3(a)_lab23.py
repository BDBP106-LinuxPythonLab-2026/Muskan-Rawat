rows= 3
columns= 4
matrix=[]
character= 65

for r in range(rows):
    row= []
    for c in range(columns):
        row.append(chr(character))
        character += 1
    matrix.append(row)

for row in matrix:
    print(row)

