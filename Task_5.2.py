my_array = [1, 3, 3, 3, 4, 2, 5, 5, 2]
array_temp = []

def find_max_min(array):
    max_dig = my_array[0]
    min_dig = my_array[0]
    for i in array:
        if max_dig < i:
            max_dig = i
        if min_dig > i:
            min_dig = i 
    return max_dig, min_dig   
print(find_max_min(my_array))