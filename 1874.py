n = int(input())
arr = []
stack = []
answer = []
maxPop = 0
for i in range(n):
    arr.append(int(input()))
    if arr[i] not in stack:
        for j in range(maxPop+1,arr[i]+1):
            stack.append(j)
            answer.append('+')

    elif stack[-1] != arr[i]:
        print('NO')
        exit()
    temp = stack.pop()
    answer.append('-')
    maxPop = max(maxPop, temp)
for _, v in enumerate(answer):
    print(v)
