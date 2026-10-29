#

def protein_energy_temp():
    def calculate_free_energy(enthalpy, entropy):
        T=int(input('enter the temperature: '))
        G =  enthalpy - (T  * entropy)

        if G < 0:
            p= 'stable'
        elif G > 0:
            p='unstable'
        else:
            p='equilibrium'

        return G, p
    enthalpy=int(input('enter the enthalpy:'))
    entropy=int(input('enter the entropy:'))
    l=calculate_free_energy(enthalpy,entropy)
    print(l)
protein_energy_temp()


