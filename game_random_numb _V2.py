import random

print('''Hej!

To jest gra, gdzie musisz odgadnąć wylosowaną liczbę.
Początkowo musisz podać zakres liczb w jakim komputer będzie losował,
a następnie odgadnąć wylosowaną wartość.

''')

rangeFrom = int(input('Podaj wartość początkową: '))
rangeTo = int(input('Podaj wartość końcową: '))
proba_max = int(input('W ilu probach odgadniesz? '))

while rangeFrom >rangeTo:
    print('Podałeś błędne zakresy: ')
    rangeFrom = int(input('Podaj wartość początkową: '))
    rangeTo = int(input('Podaj wartość końcową: '))

rand1 = int(random.randint( rangeFrom, rangeTo))
print('Liczba została wylosowana.')
hit = int(input('Podaj swoją liczbę: '))

proba = 1

while rand1 != hit and proba < proba_max:
    proba = proba + 1
    if rand1 < hit:
        hit = int(input('Za duzo, podaj mniejsza liczbe: '))
    elif rand1 > hit:
        hit = int(input('Za malo, podaj wieksza liczbe: '))
    else:
        print('Zepsułeś/aś grę! :(')

if proba == proba_max:
    print('Przegrales, skonczyla Ci sie liczba prob.')
else:
    print('Gratulacje, trafiles!')


input('Do zakonczenia programu nacisnij przycisk.')
