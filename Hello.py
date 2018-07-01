print('''

Hej!

Mamy dla Ciebie kilka interesujących faktów, ale najpierw musisz nam się przyznać do kilku rzeczy!
 ''')

name = str(input('Jak masz na imię? '))
name = name.capitalize()
bornYear = int(input('W którym roku się urodziłaś/eś? '))
weight = int(input('Wcale nie chcemy Cie o to pytac, ale przyznaj sie w koncu, ile wazysz? '))

myAge = int(2018 - bornYear)
timeFromChrist = int(bornYear * 365 *24*60*60)
moonWeight = int(weight/6)
sunWeight = float(weight* 27.1)

print(name, ', już wiemy że masz ',myAge, ' lat!')
print ('Czasem w krzyku mozemy Cie nazwac ',name.upper(),', lecz gdy nie zwracamy uwagi na wielkosc znakow to: ', name.lower(), '.')
print('czy wiesz, że od narodzin Chrystusa minelo: ',timeFromChrist,'sekund?!')
print('Czy wiesz, ze Twoja waga na ksiezycu wynosi: ', moonWeight, 'kg, a na sloncu: ', sunWeight , 'kg! Musisz zaczac cwiczyc!')
input('\n \n Aby zakonczyc, nacisnij  przycisk.')
