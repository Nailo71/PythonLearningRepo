import random

print('''Hej!

Zmiana banana, teraz Ty będziesz podawał liczbę, a komputer zgadywał!

''')

liczba = int(input('Podaj liczbę od 1 do 100: '))

if liczba < 1 or liczba > 100:
    print('Ziomek, podałeś liczbe poza zakresem...')
else:
    random = int(random.randint(1, 100))
    shoot = 1
    while random != liczba:
        shoot = shoot +1
        random = int(random.randint(1, 100))


print('ziomek, komp trafil w ', shoot , ' liczbie prob. CIekaw czy bylbys lepszy!')

input('aby zakonczyc nacisnij przycisk.')
