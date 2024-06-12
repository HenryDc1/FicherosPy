""""
Dissenyeu la funció tabletsBarats (nomf1, nomf2, p), que llegeix un fitxer de tablets nomf1 i
crea un nou fitxer anomenat nomf2 que inclou nomes els tablets que tenen un preu inferior a
p. Cada línia del fitxer de sortida representarà un tablet i tindrà el format
"""

def tabletsBarats(nomf1, nomf2,p):
    with open(nomf1,'r') as a,open(nomf2,'w') as b:
        for line in a:
            marca, model, cpu, velocitat, preu = line.strip().split(';')
            preu = float(preu)
            velocitat = int(velocitat)
            marca = marca[0:3]
            print(marca,model,preu)
            if preu < p:
                if velocitat < 500:
                    velocitat = 'Baixa'
                elif velocitat > 500 & velocitat < 900:
                    velocitat = 'Mitjana'
                else:
                    velocitat = 'Alta'
                b.write(marca+'-'+model + ' ' + velocitat +"\n")

tabletsBarats('tablets.txt','table_barata.txt',900)