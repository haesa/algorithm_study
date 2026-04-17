import sys
sys.setrecursionlimit(10**6)

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
inorder = list(map(int, read().split()))
postorder = list(map(int, read().split()))

inorder_map = {v: i for i, v in enumerate(inorder)}


def preorder(post_start, post_end, in_start, in_end):
    if post_start > post_end:
        return

    root_pos = inorder_map[postorder[post_end]]  # inorder에서 루트 노드 인덱스
    left_size = root_pos - in_start

    write(str(postorder[post_end]) + ' ')
    preorder(post_start, post_start + left_size - 1, in_start, root_pos - 1)
    preorder(post_start + left_size, post_end - 1, root_pos + 1, in_end)


preorder(0, N - 1, 0, N - 1)