n = int(input())
answer = []
for i in range(n):
    str = list(input())
    stack=[]
    for i,v in enumerate(str):
        if v =='(':
            stack.append(')')
        elif v ==')' and len(stack) == 0:
            stack.append('x')
            break
        else:
            stack.pop()
    if len(stack) == 0:
        answer.append('YES')
    else:
        answer.append('NO')

for i,v in enumerate(answer):
    print(v)
