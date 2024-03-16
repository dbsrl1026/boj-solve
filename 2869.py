import math

up, down, height = map(int, input().split())
answer = math.ceil((height-up)/(up-down) +1)
print(answer)
