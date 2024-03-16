while True:
    temp = input()
    if temp == '.':
        break
    str = list(temp)
    if not str:
        print('no')
        continue
    stack = []
    flag = 'yes'

    for i, v in enumerate(str):
        if v == '(':
            stack.append(')')
        if v == '[':
            stack.append(']')
        if v == ')' or v == ']':
            if not stack or stack[-1] != v:
                flag = 'no'
                break
            else:
                stack.pop()

        if i == len(str)-1 and v !='.':
            flag = 'no'
    if stack :
        flag = 'no'
    print(flag)
