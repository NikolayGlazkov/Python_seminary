def print_operation_table(operation, rows, columns):
    array = [[0] * columns for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            array[i][j] = operation(i + 1, j + 1)

    for row in array:
        print(*row)

# Пример использования для возведения чисел в степень:
print_operation_table(lambda x, y: x ** y, 4, 4)
