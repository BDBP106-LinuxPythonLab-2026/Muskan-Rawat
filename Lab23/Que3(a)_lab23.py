rows= 3
columns= 4
matrix=[]
character= 65

with open("stringmatrix.dat", "w") as file:
    for r in range(rows):
        row= []
        for c in range(columns):
            row.append(chr(character))
            character += 1
            matrix.append(row)
        file.write(" ".join(row) + "\n")

print("stringmatrix.dat created successfully")

