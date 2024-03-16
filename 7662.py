import sys
import heapq

test = int(sys.stdin.readline())
for _ in range(test):
    num = int(sys.stdin.readline())
    heap=[]
    maxheap = []
    index = []
    cnt = 0
    for _ in range(num):
        arr = list(map(str, sys.stdin.readline().split()))
        if arr[0] == 'I':
            val = int(arr[1])
            heapq.heappush(heap, (val,cnt))
            heapq.heappush(maxheap, (-val,cnt))
            index.append(True)
            cnt+=1
        elif arr[0] == 'D':
            if arr[1] == '1':
                while maxheap:
                    get = heapq.heappop(maxheap)[1]
                    if index[get] == True:
                        index[get] = False
                        break
            elif arr[1] == '-1':
                while heap:
                    get = heapq.heappop(heap)[1]
                    if index[get] == True:
                        index[get]= X
                        break
    answer = []
    if heap:
        for i in range(len(heap)):
            temp = heapq.heappop(heap)
            if index[temp[1]] == True:
                answer.append(temp[0])


    if answer:
        print(answer[-1], answer[0])
    else:
        print('EMPTY')