n = int(input())
if n == 1 :
    print(1)
    exit()
count =1
room = 1
while True:
    room += count*6
    count+=1
    if n <= room:
        print(count)
        exit()