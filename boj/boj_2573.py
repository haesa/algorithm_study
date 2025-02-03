# 입력: N, M, N개의 줄마다 M개의 정수 (이차원 배열의 행의 개수, 열의 개수, 배열 요소)
# 로직: 
#   - BFS 또는 DFS로 이차원 배열을 순회하며 빙산 높이 1만큼 빼기, year 1 증가
#   - BFS 또는 DFS로 총 그래프의 개수 세기
#   - 그래프 개수가 1인 경우 위 과정 반복
#   - 그래프 개수가 2인 경우 이때의 year가 문제의 답
# 출력: 빙산이 분리되는데 걸리는 연수, 빙하가 다 녹는 경우 0 출력

import sys
from collections import deque

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
origin_graph = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def valid_boundary(r, c):
  return r >= 0 and r < n and c >= 0 and c < m

# BFS
def bfs(graph, r, c, visited, sea_list):
  queue = deque()
  queue.append([r, c])

  while queue:
    current_r, current_c = queue.popleft()
    sea_count = 0
    
    if visited[current_r][current_c]:    
      continue
    
    visited[current_r][current_c] = 1

    for i in range(4):
      next_r, next_c = current_r + dr[i], current_c + dc[i]
      
      if valid_boundary(next_r, next_c):
        if graph[next_r][next_c] > 0:
          queue.append([next_r, next_c])
        else:
          sea_count += 1
    sea_list.append([current_r, current_c, sea_count])

def solution(graph):
  year = 0
  
  while True:
    count = 0 # 빙하 개수
    visited = [[0] * m for _ in range(n)]
    sea_list = []
    
    for r in range(n):
      for c in range(m):
        if graph[r][c] == 0 or visited[r][c]:
          continue

        bfs(graph, r, c, visited, sea_list)
        count += 1 # 빙산 개수 카운팅
    
    if count > 1:  # 빙산이 둘로 나뉘는 경우
      return year
    elif count == 0:
      return 0    
    
     # 빙하 깎기  
    for r, c, sea in sea_list:
      graph[r][c] -= sea
      
      if graph[r][c] < 0:
        graph[r][c] = 0
        
    year += 1

print(solution(origin_graph))