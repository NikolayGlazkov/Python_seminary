# Программа принимает от пользователя три числа :

# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


def progression(num1,num2,num3):
    array = []
    start_dig = num1
    for i in range(num3):
        array.append(start_dig)
        start_dig = start_dig+num2
    print(array)

array = [int(input(f"Введите число {i+1} :")) for i in range(3)]

progression(array[0],array[1],array[2])