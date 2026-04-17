# 입력: N, K (수빈이의 위치, 동생의 위치)
# 로직: BFS를 이용해서 동생과 만날 때까지 수빈이가 이동할 수 있는 모든 경로를 이동
# 출력: 수빈이가 동생을 찾아가는 최소 시간

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

# bfs
def bfs(start, target):
  visited = [False] * 100_101
  queue = deque([[start, 0]])
  visited[start] = True
  
  while len(queue) > 0:
    current, time = queue.popleft()
    
    if current == target:
      return time
    
    if valid_range(current + 1) and visited[current + 1] == False:
      queue.append([current + 1, time + 1])
      visited[current + 1] = True
    if valid_range(current - 1) and visited[current - 1] == False:
      queue.append([current - 1, time + 1])
      visited[current - 1] = True
    if valid_range(current * 2) and visited[current * 2] == False:
      queue.append([current * 2, time + 1])
      visited[current * 2] = True
    
def valid_range(value):
  return value >= 0 and value <= 100_000

# 최소 시간 출력
print(bfs(n, k))
