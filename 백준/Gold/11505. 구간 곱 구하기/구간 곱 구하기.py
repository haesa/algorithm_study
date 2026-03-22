import sys
import math
input = sys.stdin.readline

P = 1_000_000_007

N, M, K = map(int, input().split())

h = math.ceil(math.log2(N))  # 트리 높이
l = 2 ** h  # 말단 노드 개수
v = 2 * l - 1  # 전체 노드 개수

tree = [1] * (v + 1)
for i in range(N):
    tree[v + 1 - N + i] = int(input())

for i in range(v - l, 0, -1):
    tree[i] = (tree[i * 2] * tree[i * 2 + 1]) % P

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if (a == 1):
        i = v - N + b
        tree[i] = c

        while i // 2 > 0:
            i //= 2
            tree[i] = (tree[i * 2] * tree[i * 2 + 1]) % P

    elif (a == 2):
        left, right = v - N + b, v - N + c
        result = 1

        while left <= right:
            if left % 2 == 1:
                result = (result * tree[left]) % P
                left += 1
            if right % 2 == 0:
                result = (result * tree[right]) % P
                right -= 1

            left //= 2
            right //= 2

        print(result)
