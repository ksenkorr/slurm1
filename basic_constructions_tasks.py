
# Задача 1:
'''
Распечатать в консоль матрицу 5 на 5, заполненную числами по порядку
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''

'''
# Мое решение
for i in range(1,26):
    print(i, end=" ")
    #print(f"{i} ")
    if i % 5 == 0:
        print('\n')
'''

'''Слерм решение
for i in range(1, 26):
    if not i % 5:
        print (i)
    else:
        print (i, end=' ')
'''

#Задача 2:
'''
Напишите программу, которая принимает из консоли число и распечатывает треугольную таблицу высотой в это число, 
заполненную числами по порядку. Пример для пользовательского числа 4:

1

2 3

4 5 6

7 8 9 10
'''

# Мое решение
'''
a = int(input())
k = 1

for i in range (1, a+1):

    for j in range (1, i+1): 
        print(k, end=" ")
        k = k + 1

    # Перевод на другую строку. Если писать print('\n'), то помимо перевода будет еще пустая строка
    print()
'''

'''
# Слерм решение
value = int(input())
 
count = 0
for i in range(value):
    for _ in range(i + 1):
        count += 1
        print (count, end=' ')
    print()
'''


# Задача 3
'''
Напишите программу, которая принимает из консоли число и распечатывает треугольную таблицу высотой в это число, 
заполненную числами в порядке уменьшения. Пример для пользовательского числа 4:

       10

      9 8

   7 6 5

4 3 2 1
'''

# Мое решение
'''
value = int(input())
count = int(value * (value+1) / 2)

for i in range (value):

    for n in range (value-i):
        print(end="   ")
    

    for _ in range (i+1):     
        if count < 10:
            print("  ", end="")
        else:
            print(" ", end="")
        
        print(count, end="")        
        count -= 1

    # Перевод на другую строку. Если писать print('\n'), то помимо перевода будет еще пустая строка
    print()   
'''

# Слерм решение №1
'''
value = int(input())
count = 1
rows = []
 
for i in range(value, 0, -1):
    row = []  
    for _ in range(i):        
        row.append(count)
        count += 1
    rows.append(reversed(row))    
       
for row in reversed(rows):    
    r = ' '.join(map(str, row))      
    print(f"{r:>{value * 3}}")
'''
'''
# Слёрм решение №2
value = int(input())
row_count = 1
row = []
 
for i in range(value**2 - sum(range(value)), 0, -1):  
    row.append(i)  
    
    if len(row) == row_count:
        line = ' '.join(map(str, row))
        
        print (f'{line:>{value*3}}')
        row = []
        row_count += 1
'''