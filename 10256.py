# from collections import deque
#
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.failure = None
#         self.end = False
#
# t = int(input())
#
# for _ in range(t):
#     len_dna, len_marker = map(int, input().split())
#     dna = list(input())
#     marker = list(input())
#
#     root = TrieNode()
#
#     mutants = set()
#     mutants.add(tuple(marker))
#
#     for i in range(len_marker - 1):
#         for j in range(i + 2, len_marker + 1):
#             mutant = tuple(marker[:i] + list(reversed(marker[i:j])) + marker[j:])
#             mutants.add(mutant)
#
#     for mutant in mutants:
#         node = root
#         for char in mutant:
#             node = node.children.setdefault(char, TrieNode())
#         node.end = True
#
#     queue = deque()
#     for child in root.children.values():
#         child.failure = root
#         queue.append(child)
#
#     while queue:
#         current = queue.popleft()
#         for char, next_node in current.children.items():
#             f = current.failure
#             while f and char not in f.children:
#                 f = f.failure
#             next_node.failure = f.children[char] if f and char in f.children else root
#             next_node.end |= next_node.failure.end  # 탐색 도중 일치여부 반영
#             queue.append(next_node)
#
#     cnt = 0
#     node = root
#     for char in dna:
#         while node and char not in node.children:
#             node = node.failure
#         node = node.children[char] if node and char in node.children else root
#         if node.end:
#             cnt += 1
#
#     print(cnt)
t = int(input())

for _ in range(t):
    len_dna, len_marker = map(int, input().split())
    dna = input()
    marker = list(input())

    mutants = set()
    mutants.add("".join(marker))

    for i in range(len_marker - 1):
        for j in range(i + 2, len_marker + 1):
            mutant = marker[:i] + list(reversed(marker[i:j])) + marker[j:]
            mutants.add("".join(mutant))

    cnt = 0
    for i in range(len_dna - len_marker + 1):
        window = dna[i:i + len_marker]
        if window in mutants:
            cnt += 1

    print(cnt)
