def sum_of_difit(num):
    summa = 0
    while num > 0:
        summa += num%10
        num = num//10
    return(summa)

print(sum_of_difit(321))

    