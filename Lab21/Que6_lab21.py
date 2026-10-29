#to find the total number of ATP

def cell_metabolism(g,o):
    def energy_output():
        if o == 6 * g:
            nATP= 38 * g
        elif g > (o/6):
            nATP= 38 * (o/6)
        elif g < (o/6):
            nATP= 38 *g
        return nATP
    return energy_output()

g=int(input("enter the number of glucose: "))
o=int(input("enter the number of oxygen "))
k=cell_metabolism(g,o)
print("the total number of ATP produced= ",k)


