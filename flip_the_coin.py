import random
print('''Hej!

Ten program rzuci monetą tyle razy, ile mu wyznaczysz, a następnie
pokaże ile razy wypadła reszka a ile orzeł.

''')

roll = int(input('Ile razy rzucamy monetą? '))
x = int(0)
reszka = int(0)
orzel = int(0)

while x < roll:
    rand = int(random.randint( 0 , 1))
    x = x + 1
    if rand == 0:
        reszka = reszka +1
    else:
        orzel = orzel +1


print('Orzel wynosi:', orzel)
print('Reszka wynosi:', reszka)


input('zaby zamknac program nacisnij przycisk')
