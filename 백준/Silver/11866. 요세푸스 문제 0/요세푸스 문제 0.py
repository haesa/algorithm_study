import sys
from collections import deque

read = sys.stdin.readline
write = sys.stdout.write

N, K = list(map(int, read().split()))
queue = deque(range(1, N + 1))

result = []
while queue:
  queue.rotate(-(K - 1))
  result.append(queue.popleft())
  
write('<' + ', '.join(map(str, result)) + '>')