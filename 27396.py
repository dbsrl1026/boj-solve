arr, n = input().split()
arr = list(arr)
n = int(n)

dict = {}
for _ in range(n):
    q = input()
    if q == '2':
        for i in range(len(arr)):
            if arr[i] in dict:
                arr[i] = dict[arr[i]]
        print(''.join(arr))
        dict = {}
    else:
        q, i1, i2 = q.split()
        for key, value in dict.items():
            if value == i1:
                dict[key] = i2
        if i1 not in dict and i1 != i2:
            dict[i1] = i2
