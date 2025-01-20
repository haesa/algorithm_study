# 입력: N, M, V (정점의 개수, 간선의 개수, 시작 번호)
# 로직: DFS, BFS 함수
# 출력 : DFS, BFS 수행 결과를 한 줄씩 출력

import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

# 행렬 만들기
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트
visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)

# dfs
def dfs(v):
  answer = []
  stack = [v]
  
  while len(stack) > 0:
    current = stack.pop()

    if visited_dfs[current] == 1:
      continue
        
    visited_dfs[current] = 1
    answer.append(current)
    
    for next in range(n, 0, -1):
      if graph[current][next] == 1 and visited_dfs[next] == 0:
        stack.append(next)

  return answer

# bfs
def bfs(v):
  answer = []
  queue = [v]
  visited_bfs[v] = 1
  
  while len(queue) > 0:
    current = queue.pop(0)
    answer.append(current)
    
    for next in range(0, n + 1):
      if graph[current][next] == 1 and visited_bfs[next] == 0:
        queue.append(next)
        visited_bfs[next] = 1

  return answer
  
# dfs, bfs 결과 출력
print(' '.join(map(str, dfs(v))))
print(' '.join(map(str, bfs(v))))