def calculate(arr):
    l = len(arr)
    for i in range(l):
        if arr[i] == ')':
            return calculate(arr[:i])+ [''] + arr[i + 1:]
        if arr[i] == '(':
            arr = arr[:i] + [''] + calculate(arr[i + 1:])

    for i in range(l):
        if arr[i] == '*' or arr[i] == '/':
            for j in range(i-1,-1,-1):
                if arr[j]!='':
                    d1 = arr[j]
                    arr[j] =''
                    break
            for j in range(i+1,l):
                if arr[j]!='':
                    d2 = arr[j]
                    arr[j]= ''
                    break
            arr[i] = str(d1+d2+arr[i])
    for i in range(l):
        if arr[i] == '+' or arr[i] == '-':
            for j in range(i - 1, -1, -1):
                if arr[j] != '':
                    d1 = arr[j]
                    arr[j] = ''
                    break
            for j in range(i + 1, l):
                if arr[j] != '':
                    d2 = arr[j]
                    arr[j] = ''
                    break
            arr[i] = str(d1 + d2 + arr[i])
    return arr


arr = list(input())
result = ''.join(map(str, calculate(arr)))
print(result)