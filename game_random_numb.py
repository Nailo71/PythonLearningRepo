import random

print('''Hej!

To jest gra, gdzie musisz odgadnąć wylosowaną liczbę.
Początkowo musisz podać zakres liczb w jakim komputer będzie losował,
a następnie odgadnąć wylosowaną wartość.

''')

rangeFrom = int(input('Podaj wartość początkową: '))
rangeTo = int(input('Podaj wartość końcową: '))

while rangeFrom >rangeTo:
    print('Podałeś błędne zakresy: ')
    rangeFrom = int(input('Podaj wartość początkową: '))
    rangeTo = int(input('Podaj wartość końcową: '))

rand1 = int(random.randint( rangeFrom, rangeTo))
print('Liczba została wylosowana.')
hit = int(input('Podaj swoją liczbę: '))

while rand1 != hit:
    if rand1 < hit:
        hit = int(input('Za duzo, podaj mniejsza liczbe: '))
    elif rand1 > hit:
        hit = int(input('Za malo, podaj wieksza liczbe: '))
    else:
        print('Zepsułeś/aś grę! :(')

print('Gratulacje, trafiles!')

input('Do zakonczenia programu nacisnij przycisk.')
