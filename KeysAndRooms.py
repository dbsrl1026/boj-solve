from collections import deque


def completeSearch(room):
    visited = []
    length = len(room)

    def bfs():
        queue = deque()
        queue.append(0)
        while queue:
            curRoom = queue.popleft()
            visited.append(curRoom)
            nextRoom = room[curRoom]
            for v in nextRoom:
                if v not in visited:
                    queue.append(v)

    bfs()
    #for i in range(length):
    #    if i not in visited:
    #        return False
    # return True
    if len(visited) == len(room): return True
    else: False



ans = completeSearch(room=[[1, 3], [2, 4], [0], [4], [], [3, 4]])
print(ans)
