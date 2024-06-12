"""
Exercici 4.
Escriure un programa que rebi un arxiu, ho llegeixi i imprimeixi per pantalla
quantes línies, quantes paraules i quants caràcters conté l'arxiu.
"""
with open('copiar.txt', 'r') as f:
    lineas = 0
    palabras = 0
    caracters = 0
    for line in f:
        lineas+=1
        palabras+= len(line.split())
        caracters+= len(line)
    print(palabras)
    print(caracters)
    print(lineas)