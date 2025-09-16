import sys
sys.setrecursionlimit(10000)
tc= int(input())
for _ in range(tc):
    length = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    def dnq(pre_s, pre_e, in_s, in_e):
        if pre_s - pre_e == 0:
            return []
        if pre_s - pre_e == 1:
            return preorder[pre_s:pre_e]
        pivot = preorder[pre_s]
        for i in range(in_s, in_e):
            if inorder[i] == pivot:
                pre_slice = pre_s + 1 + i - in_s
                return dnq(pre_s + 1, pre_slice, in_s, i) + dnq(pre_slice, pre_e, i + 1, in_e) + [pivot]

    postorder = dnq(0,length,0,length)
    print(*postorder)
