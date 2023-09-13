# - Аргументы: список чисел и границы диапазона
#num1 - от этой цифры
#num2 - до этой
def function_index_dig(array,num1,num2):
    answer = []
    for i in range(len(array)):
        if num1 <= array[i] <= num2:
            answer.append(f"({array[i]},{array.index(array[i])})")
    return answer
    
lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

print(*function_index_dig(lst1, 2, 10))