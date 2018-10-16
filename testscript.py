import math
from time import sleep

def printLogarithm(x):
    if x <= 0:
        print "Positive numbers only, please."
        return
    result = math.log(x)
    print "The log of x is", result

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

print(area(input('give the circle radius: ')))


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
