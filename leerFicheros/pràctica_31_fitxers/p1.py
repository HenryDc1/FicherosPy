with open('pacientes.txt', 'r') as a, open('filtro.txt', 'w') as b:
    next(a)
    for line in a:
        nom,edat,diabetico = line.split()
        edat = int(edat)
        if edat > 20 :
            if diabetico == 'No':
                b.write(nom + '\n')
    print(nom,edat,diabetico)