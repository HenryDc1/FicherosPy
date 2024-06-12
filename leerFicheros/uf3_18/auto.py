auto = open('arxiu1.txt', 'w')
for i in range(27):
    auto.write('Linea' + str(i) + '\n')  # Converteix i a cadena i afegeix un salt de línia
auto.close()  # No oblidis tancar l'arxiu després d'escriure
