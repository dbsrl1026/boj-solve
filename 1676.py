import math

N = int(input())
result = math.factorial(N)
result = list(str(result))
count = 0
for i in range(len(result)-1,-1 ,-1):
    if result[i] != '0':
        print(count)
        exit()
    count+=1