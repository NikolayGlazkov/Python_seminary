# # Напишите функцию, которая принимает натуральное число n, в теле функции считывает (input) последовательность из n элементов
# # Возвращает эту последовательность в виде строки в обратном порядке
# # Примеры/Тесты:
# <function_name>(5) 1 2 3 4 5 -> '5 4 3 2 1'
# <function_name>(4) q w e r -> 'r e w q'
# <function_name>(3) 8 7 9 -> '9 7 8'
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# def reversed_temp(num):
#     simval = input()
#     if num == 1:
#         return simval
#     return simval + " " + reversed_temp(num-1) 
# print(reversed_temp(3))

# f 
# g 
# h 
# f g h 


array = [1, 1, 1, 2, 3, 7]
array1 = []

min_dig = min(array)
max_dig = max(array)


for i in range(len(array)):
    if array[i] == min_dig:
        array1[i] = max_dig
    else:
        array1[i] = array[i]

print(array1)
