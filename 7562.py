from collections import deque

dx=[-1,-2,-2,-1,1,2,2,1]
dy=[2,1,-1,-2,-2,-1,1,2]

n= int(input())

for i in range(n):
    l =int(input())
    chess=[]
    for i in range(l):
        chess.append([0]*l)
    queue=deque()
    x,y=map(int,input().split())
    destX, destY = map(int, input().split())
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if x==destX and y==destY:
            break
        for j in range(8):
            tmpX=x+dx[j]
            tmpY=y+dy[j]
            if tmpX<0 or tmpY<0 or tmpX>=l or tmpY>=l:
                continue
            if chess[tmpX][tmpY]==0:
                chess[tmpX][tmpY]=chess[x][y]+1
                queue.append((tmpX,tmpY))
    print(chess[destX][destY])