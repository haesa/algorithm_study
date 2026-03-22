import sys
import math
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

h = math.ceil(math.log2(N))  # 트리 높이
l = 2 ** h  # 말단 노드 개수
v = 2 * l - 1  # 전체 노드 개수
tree = [0] * (v + 1)

for i in range(N):  # 말단 노드 채우기
    tree[v + 1 - N + i] = nums[i]

for i in range(l - 1, 0, -1):  # 부모 노드 채우기
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if (a == 1):
        cur = v - N + b
        tree[cur] = c
        while cur > 1:
            parent = cur // 2
            tree[parent] = tree[parent * 2] + tree[parent * 2 + 1]
            cur = parent
    elif (a == 2):
        left, right = v - N + b, v - N + c
        result = 0

        while left <= right:
            if left % 2 == 1:
                result += tree[left]
                left += 1
            if right % 2 == 0:
                result += tree[right]
                right -= 1

            left //= 2
            right //= 2

        print(result)
