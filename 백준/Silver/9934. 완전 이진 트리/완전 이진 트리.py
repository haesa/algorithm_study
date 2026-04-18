import sys
from collections import deque

read = sys.stdin.readline

K = int(read())
inorder = list(map(int, read().split()))


def bfs():
    result = []
    q = deque([(K, 0, len(inorder) - 1)])

    while q:
        k, start, end = q.popleft()

        # 서브트리가 없는 경우 다음 반복으로 이동
        if start > end:
            continue

        full_tree_size = 2**k - 1  # 완전 이진 트리가 꽉 차 있는 경우 크기
        tree_size = end - start + 1  # 현재 트리의 크기

        # 마지막 레벨에서 노드가 절반이상 찼는지 확인, 그에 따라 왼쪽 서브트리의 크기를 결정
        left_size = 2**(k-1) - 1 if tree_size >= full_tree_size - \
            2**(k-2) else tree_size - 2**(k-2)
        # inorder에서의 루트의 위치 확인
        root_pos = start + left_size
        # 루트 노드 result에 추가
        result.append(inorder[root_pos])

        # 마지막 레벨에서 노드가 절반을 넘었는지 확인, 그에 따라 오른쪽 서브트리의 k를 결정
        right_next_k = k - 1 if tree_size > full_tree_size - \
            2**(k-2) else k - 2

        q.append((k - 1, start, root_pos - 1))
        q.append((right_next_k, root_pos + 1, end))

    return result


result = bfs()
i = 0
for k in range(1, K + 1):
    while i < 2**(k) - 1:
        print(result[i], end=' ')
        i += 1
    print('')
