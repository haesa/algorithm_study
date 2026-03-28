import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

calc_list = [lambda x: x * 2, lambda x: x * 10 + 1]

result = -1
q = deque([(A, 1)])
while q:
    n, cnt = q.popleft()

    if n == B:
        result = cnt
        break

    for calc in calc_list:
        nxt = calc(n)
        if nxt <= B:
            q.append((nxt, cnt + 1))

print(result)
