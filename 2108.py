

def choiBin(arr,n):

    dic = {}
    for i,v in enumerate(arr):
        if v in dic:
            dic[v] += 1
        else:
            dic[v] = 1
    maxvalue = max(dic.values())
    arrr = []
    for k,v in dic.items():
        if v == maxvalue:
            arrr.append(k)
    if len(arrr) == 1:
        return arrr[0]
    else:
        arrr = sorted(arrr)
        return arrr[1]


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr)

average = round(sum(arr)/n)
mid = arr[int(n/2)]
often = choiBin(arr,n)
bumwi = max(arr) - min(arr)
print(average)
print(mid)
print(often)
print(bumwi)
