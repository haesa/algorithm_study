import sys
from collections import deque

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

q = deque(range(1, N + 1))

while len(q) > 1:
  q.popleft()
  q.append(q.popleft())
    
write(str(q[0]))
