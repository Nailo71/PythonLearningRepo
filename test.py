#binary calculation

#word = ord(input('Podaj wartosc: '))

def getBinary(value):
    binary = ''
    while value > 0:
        if value%2 == 1:
            value = (value-1)/2
            binary = binary + '1'
        elif value%2 == 0:
            value = value /2
            binary = binary + "0"
        else:
            break
    print(binary)


def getBinaryArray(value):
    binary = [0,0,0,0,0,0,0,0]
    i = 8
    while value > 0:
        if value%2 == 1:
            value = (value-1)/2
            binary[i-1] = 1
        elif value%2 == 0:
            value = value /2
            binary[i - 1] = 0
        else:
            break
        i= i -1
    print(binary)

value = ord('C')
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
binary = [0,0,0,0,0,0,0]
i = 7
while value > 0:
    if value%2 == 1:
        value = (value-1)/2
        binary[i-1] = 1
    elif value%2 == 0:
        value = value /2
        binary[i - 1] = 0
    i= i -1

chuckCode = ''
i= 0
count1=0
count2=0
while i < len(binary):
    if binary[i] == 1:
        while binary[i] == 1:
            i = i+1
            count1 = + 1
        chuckCode = '0 '+ count1*'0'
    elif binary[i] == 0:
        while binary[i] == 0:
            i = i+1
            count2 = + 1
        chuckCode = '00 '+ count1*'0'



print(chuckCode)