import math
from time import sleep

def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        sleep(1)
        countdown(n-1)

def area(radius):
    temp = math.pi * radius**2
    return temp

def compareFun(x, y):
    if x>y:
        return 1
    elif x==y:
        return 0
    elif x<y:
        return -1

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def hypotheneus(a, b):
    da =a**2
    db = b**2
    c = da+db
    return math.sqrt(c)

def circleField(c1, c2, s1, s2):
    radius= distance(c1, c2, s1, s2)
    result = area(radius)
    return result



def newLine():
    print('')

def getShitDone():
    task = input('Give me your task difficulty from 1 to 5: ')
    time = input('How much time do you have for it in hours: ')
    effort = task*time
    if effort > 20:
        print('Dude, you are fucked!')
    else:
        print('Come one, you can do that!')


def justNewFunction(tomasz, weather):
    alexis = tomasz*weather+weather
    print(alexis);

def isDivisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def isBetween(x, y, z):
    return y <= x <= z

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def countDown(n):
    while n>0:
        print(n)
        n = n-1
    print('Jebudup')

def displayMany(x):
    while x>0:
        print('komunikat')
        x= x-1

def sequence(n):
    while n != 1:
        print(n)
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1

def nLine(n):
    while n>0:
        print('bruce')
        n =n-1

'''
x = 1.0
while x < 10.0:
    print(x , '\t' , math.log(x)/math.log(2.0)) 
    x = x + 1.0
'''

# print('produces', '\n', '\t'*2, 'this', '\n', '\t'*4 ,'output.') # '\t' -> tabulator, '\n' -> nowa linia

'''
i = 1
while i <= 6:
    print(2*i, ' '), # przecinek sprawia, ze wyswietlenie nastepnej linijki txt jest od nowej linii <jak enter>
    i = i + 1
print()
'''

def printMultiples(n):
    i = 1
    while i <= 6:
        print(n*i, '\t'),
        i = i + 1
    print()

def printMultTable(high):
    i = 1
    while i <= high:
        printMultiples(i)
        i = i + 1


def backpedal(word):
    i = 0
    j = -1
    while i<len(word):
        print(word[j])
        i = i+1
        j = j-1

def test(word):
    t=0
    for char in word:
        if char =='t':
            t= t+1
    print(t)
def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1

print(find('tmaszooooo', 'o'))