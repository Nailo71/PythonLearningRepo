import random

print('''Hej!

Pick your number.
You have to declare number range that random number will be picked then you have to say that number is that.
''')

rangeFrom = int(input('From range: '))
rangeTo = int(input('To range: '))
user_max_try = int(input('How many tries do you need? '))

while rangeFrom >rangeTo:
    print('Incorrect range: ')
    rangeFrom = int(input('From range: '))
    rangeTo = int(input('To range: '))

rand1 = int(random.randint( rangeFrom, rangeTo))
print('We know the number!')
hit = int(input('Give a shot: '))

user_try = 1

while rand1 != hit and user_try < user_max_try:
    user_try = user_try + 1
    if rand1 < hit:
        hit = int(input('Too high, picker lower: '))
    elif rand1 > hit:
        hit = int(input('Too low, pick greater: '))
    else:
        print('You broke it! :(')

if user_try == user_max_try:
    print('You lost, too many tries.')
else:
    print('Score, perfect! YOu won!')

input('Hit button to close the program.')
