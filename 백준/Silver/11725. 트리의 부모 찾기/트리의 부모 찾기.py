import sys
from collections import deque

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  a, b = map(int, read().split())
  graph[a].append(b)
  graph[b].append(a)

parent = [0] * (N + 1)
q = deque([1])

while q:
  parent_node = q.popleft()
  for cur_node in graph[parent_node]:
    if parent[cur_node]:
      continue
    parent[cur_node] = parent_node
    q.append(cur_node)

write('\n'.join(map(str, parent[2:])))