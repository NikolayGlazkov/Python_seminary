def gud_tikit(num):
    answer = 0
    while num > 0:
        answer += num%10
        num = num//10
    return answer

    
n =  385316
if gud_tikit(int(str(n)[:3])) == gud_tikit(int(str(n)[3:])):
    print("yes")
else:
    print("no")

