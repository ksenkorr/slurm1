import random

'''
Задача №4
Напишите игру “Угадай число”. Программа загадывает число от 0 до 100, пользователь должен угадать число за 8 попыток. Если попытки заканчиваются, пользователь проиграл. При каждой неудачной попытке программа сообщает больше или меньше загаданное число.

Число загадано! Попытка №1:

50

Не правильно! Загаданное число больше!

Попытка №2

75

Не правильно! Загаданное число больше!

Попытка №3

87

Не правильно! Загаданное число меньше!

Попытка №4

81

Не правильно! Загаданное число меньше!

Попытка №5

Не правильно! Загаданное число больше!

Попытка №6

79

Вы победили!
'''

'''
# Мое решение
a = random.randint(0,100)
print("Число загадано!", end=" ")

for i in range (1, 9):
    print (f'Попытка № {i}:')
    b = int(input())
    if a == b:
        print ('Вы победили!')
        break
    elif a > b:
        print ("Неправильно! Загаданное число больше!")
    elif a < b:
        print ("Не правильно! Загаданное число меньше!")
    

# Слерм решение
from random import randint
 
secret = randint(0, 100)
 
print ('Число загадано! Попытка №1:')
user_number = int(input())

for i in range(2, 9):
    if user_number == secret:
        print ("Вы победили!")
        break
    
    word = 'меньше' if user_number > secret else 'больше'
    print(f'Не правильно! Загаданное число {word}!')
    print(f'Попытка №{i}')
    user_number = int(input())
else:
    print ('Вы проиграли!')
'''

'''
Задача № 5:

Напишите игру “Угадай число”. Пользователь загадывает число от 0 до 100, программа должна угадать число за 8 попыток. При каждой неудачной попытке пользователь должен сообщать программе больше(+) или меньше(-) число он задумал, если программа отгадала число, должен написать =.

Попытка №1: Это число 50?

-

Попытка №2: Это число 25?

-

Попытка №3: Это число 13?

-

Попытка №4: Это число 7?

+

Попытка №5: Это число 10?

+

Попытка №6: Это число 12?

-

Попытка №7: Это число 11?

=

Ура, я победил!
'''

# Мое решение (за базу взято прошлое решение слерм)
# Вариант 1
'''
secret = int(input())

while secret> 100 or secret < 0:
    print ('Загаднное число должно быть от 0 до 100, попробуйте еще раз.')
    secret = int(input())

for i in range(1, 9):
    program_number = random.randint(0, 100)

    print(f'Попытка №{i}: Это число {program_number}?')

    if program_number == secret:
        print ("Ура, я победил!")
        break

    if secret < program_number:
         word = '-'
    elif secret > program_number:
        word = '+'
    else:
        word = '='

    print(f'{word}')

    if i == 8:
        print ('Попытки закончились!')
    
'''

# Слерм решение
# Отличается от моего, поняла не так.

number = 50
step = 50

for i in range(1, 9):
    print (f'Попытка №{i}: ', end='')
    print (f'Это число {number}?')

    char = input()
    
    step = round(step/2)
    if char == '=':
        print('Ура, я победил!')
        break
    elif char == '-':
        number -= step
    else:
        number += step
else:
    print('Я проиграл...')

