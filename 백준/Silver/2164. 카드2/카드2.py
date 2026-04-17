import sys
from collections import deque

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

q = deque(range(1, N + 1))

while len(q) > 1:
  q.popleft()
  if len(q) > 1:
    top = q.popleft()
    q.append(top)
    
write(str(q[0]))
