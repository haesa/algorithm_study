
# 입력: N, N 줄에 걸쳐 N개의 자료 (지도의 크기, 지도)
# 로직: DFS로 지도 전체를 탐색하면서 단지수 카운트
# 출력: 총 단지수와 각 단지에 속하는 집의 수를 오름차순으로 출력

import sys
from collections import deque

input = sys.stdin.readline

# 입력
n = int(input())

map_list = []
for _ in range(n):
  map_list.append(list(map(int, input().strip())))

visited = [[0] * n for _ in range(n)]
d_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def valid_boundary(r, c):
  return r >= 0 and r < n and c >= 0 and c < n

#dfs
def dfs(graph, r, c):
  count = 0
  stack = [[r, c]]
  
  while len(stack) > 0:
    current_r, current_c = stack.pop()
    
    if visited[current_r][current_c] or graph[current_r][current_c] == 0:
      continue
    
    visited[current_r][current_c] = 1
    count += 1
    
    for dr, dc in d_list:
      next_r, next_c = current_r + dr, current_c + dc
      
      if valid_boundary(next_r, next_c):
        stack.append([next_r, next_c])

  return count
  
# bfs
def bfs(graph, r, c):
  count = 0
  queue = deque([[r, c]])
  
  while len(queue) > 0:
    current_r, current_c = queue.popleft()
    
    if visited[current_r][current_c] or graph[current_r][current_c] == 0:
      continue
    
    visited[current_r][current_c] = 1
    count += 1
    
    for dr, dc in d_list:
      next_r, next_c = current_r + dr, current_c + dc
      
      if valid_boundary(next_r, next_c):
        queue.append([next_r, next_c])

  return count

# 출력
result = []
for r in range(n):
  for c in range(n):
    if map_list[r][c] == 1 and visited[r][c] == 0:
      result.append(dfs(map_list, r, c))

result.sort()

print(len(result))
for answer in result:
  print(answer)