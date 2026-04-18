import sys

read = sys.stdin.readline

preorder = []
inorder = []
position_map = {}


def make_postorder(pre_start, pre_end, in_start, in_end):
    if pre_start > pre_end or in_start > in_end:
        return []

    root_pos = position_map[preorder[pre_start]]
    left_size = root_pos - in_start
    left = make_postorder(pre_start + 1, pre_start +
                          left_size, in_start, root_pos - 1)
    right = make_postorder(pre_start + left_size + 1,
                           pre_end, root_pos + 1, in_end)

    return [*left, *right, preorder[pre_start]]


T = int(read())
for _ in range(T):
    N = int(read())
    preorder = list(map(int, read().split()))
    inorder = list(map(int, read().split()))
    position_map = {v: i for i, v in enumerate(inorder)}
    postorder = make_postorder(0, N - 1, 0, N - 1)
    print(*postorder)
