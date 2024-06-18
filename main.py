import random

print("Hello world")

print("Hello world 1")

"""
if True:
    print('True')


x = 10
if x > 10:
    print('> 10')
elif x < 5:
    print ('<5')
elif x == 10:
    print('10')
else:
    print('True')


a = int(input())
if a > 10:
    print ('a > 10')
elif a < 5:
    print ('a < 5')
else:
    print (f'a = {a}')


    a = random.randint(1,3)
    b = int(input())

    if a == b:
        print ('Yes')
    else:
        print('No!')


a = random.randint(1,3)
b = 0

while a != b:
    b = int(input())
else:
    print('Yes!')



a = random.randint(1,5)

for i in range (1, 4):
    print (f'Попытка номер {i}')
    b = int(input())
    if a == b:
        print ('Yes!')
        break

"""

def hypot (a: float, b: float) -> float:
    print (f'a = {a}, b = {b}')
    return (a*a + b*b)**0.5

#print(hypot (4, 3))

print(hypot (b=4, a=3))