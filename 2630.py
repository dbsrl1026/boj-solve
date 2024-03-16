import sys

def DnQ(n, arr, white, blue):
    if all(1 not in line for line in arr):
        return white + 1, blue
    elif all(0 not in line for line in arr):
        return white, blue + 1
    else:
        sub = []
        for i in range(int(n / 2)):
            sub.append(arr[i][:int(n / 2)])
        white, blue = DnQ(int(n / 2), sub, white, blue)
        sub = []
        for i in range(int(n / 2)):
            sub.append(arr[i][int(n / 2):])
        white, blue = DnQ(int(n / 2), sub, white, blue)
        sub = []
        for i in range(int(n / 2), n):
            sub.append(arr[i][:int(n / 2)])
        white, blue = DnQ(int(n / 2), sub, white, blue)
        sub = []
        for i in range(int(n / 2), n):
            sub.append(arr[i][int(n / 2):])
        white, blue = DnQ(int(n / 2), sub, white, blue)
    return white,blue

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
white, blue = DnQ(n, arr, 0, 0)
print(white)
print(blue)