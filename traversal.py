from collections import deque


class Node:
    def __init__(self,value =0,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)


def bfs(root):
    visited = []
    if root is None:
        return 0;
    q = deque()
    q.append(root)
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited


def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)

