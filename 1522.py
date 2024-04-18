arr = input()
olen = len(arr)
wind = arr.count('a')

arr += arr
minn = float('inf')
for i in range(olen):
    minn = min(minn, arr[i:i+wind].count('b'))
print(minn)