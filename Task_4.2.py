input_temp = "11, 92, 1, 42, 15, 12, 11, 81"#input()
# Output1: Макс. кол-во ягод 21, собрано для куста 7
answer = input_temp.replace(",","")
array = [int(x) for x in answer.split()]
print(array)

arr_count = []
for i in range(len(array)):
       arr_count.append(array[i-2] + array[i-1] + array[i])
print(max(arr_count))