# '''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.'''

def find_numbers(sum_val, product_val):
    for x in range(1, sum_val):
        y = sum_val - x
        if x * y == product_val:
            return x, y
    return None, None

sum_value = int(input("Введите сумму :"))
product_value = int(input("Введите произведение :"))

x, y = find_numbers(sum_value, product_value)

if x is not None and y is not None:
    print(f"Числа: {x} и {y}")
else:
    print("Не удалось найти подходящие числа.")



