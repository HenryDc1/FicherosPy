fusio = open('1a100.txt', 'w')
parells = open('parells.txt', 'r')
senars = open('senars.txt', 'r')

p=parells.readlines()
s=senars.readlines()

parells.close()
senars.close()

for p_line, s_line in zip(p, s):
    # Escriu la línia senar seguida de la línia parell
    fusio.write(s_line)
    fusio.write(p_line)

fusio.close()
#Leer los dos ficheros
#Escribir