''' На столе лежат n монеток. Некоторые из них 
лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же 
стороной. Выведите минимальное количество монет, которые нужно перевернуть. 
Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.'''


kolvo = int(input("Введите кол-во монет: "))

array_temp = [int(input(f'Положение монеты {i+1}:')) for i in range(kolvo)]

if array_temp.count(0) < array_temp.count(1):
    print(f"нужно перевернуть {array_temp.count(0)}")
else:
    print(f"нужно перевернуть {array_temp.count(1)}")
