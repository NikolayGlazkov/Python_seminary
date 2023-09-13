# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# https://ru.wikipedia.org/wiki/Числа_Фибоначчи

# Требуется найти N-е число Фибоначчи. Напишите рекурсивную функцию. Обратите внимание, что функция должна возвращать число.

# Примеры/Тесты:

# <function_name>(0) -> 0

# <function_name>(2) -> 1

# <function_name>(9) -> 34

# 0 1 1 2 3 5 8 13 21 34

def fibanachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibanachi(n-1)+fibanachi(n-2)
    
# 9 число = fib7 + fib8
# 

print(fibanachi(9))
    