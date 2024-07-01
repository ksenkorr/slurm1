#Задача 1:
#Напишите  функцию my_range(stop: float, start: float = 0.0, step: float =1.0) -> list[float]:

# Мое решение
def my_range(stop: float, start: float = 0.0, step: float =1.0) -> list[float]:
    return list[stop, start, step]

print (my_range(stop = 10))
print (my_range(stop = 10, start = 2, step = 2))
