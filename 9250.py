from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.failure = None
        self.end = False


len_patterns = int(input())
patterns = []
for i in range(len_patterns):
    patterns.append(list(input()))

len_texts = int(input())
texts = []
for i in range(len_texts):
    texts.append(list(input()))

root = TrieNode()

for p_str in patterns:
    node = root
    p_len = len(p_str)
    for char in p_str:
        node = node.children.setdefault(char, TrieNode())
    node.end = True

queue = deque()
for node in root.children.values():
    node.failure = root
    queue.append(node)

while queue:
    curr_node = queue.popleft()
    for char, next_node in curr_node.children.items():
        f = curr_node.failure
        while f and char not in f.children:
            f = f.failure

        if f:
            next_node.failure = f.children[char]
        else:
            next_node.failure = root

        next_node.end = next_node.end or next_node.failure.end
        queue.append(next_node)

answer = []

for text in texts:
    curr_node = root
    is_exist = False
    for i in range(len(text)):
        char = text[i]

        while curr_node and char not in curr_node.children:
            curr_node = curr_node.failure

        if curr_node:
            curr_node = curr_node.children[char]
        else:
            curr_node = root

        if curr_node.end:
            is_exist = True
            break
    if is_exist:
        answer.append("YES")
    else:
        answer.append("NO")

for a in answer:
    print(a)

