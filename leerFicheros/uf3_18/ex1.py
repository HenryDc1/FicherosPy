
parells = open('parells.txt', 'w')
for num in range(1, 101):
        if num % 2 == 0:
            parells.write(str(num) + '\n')
parells.close()

senars = open('senars.txt', 'w')
for num in range(1, 101):
        if num % 2 != 0:
            senars.write(str(num) + '\n')
senars.close()
