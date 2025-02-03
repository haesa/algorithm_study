# 입력: K, V, E (테스트 케이스, 정점의 개수, 간선의 개수)
# 로직:
#   - 주어진 간선 정보를 기반으로 인접 리스트 생성
#   - 1번 노드부터 BFS 시작
#   - 첫 방문인 경우 현재 노드에 대한 인접 노드들을 set1과 set2와 비교
#   - 교집합이 없는 경우 인접 노드가 없다는 의미이므로 해당 집합에 노드 추가
#   - set1과 set2 모두 교집합이 존재하는 경우 두 집합 모두 인접 노드가 존재한다는 의미이므로 이분 그래프 성립 불가능
# 출력: 각 테스트 케이스에 대한 이분 그래프 사실 여부를 'YES' or 'NO'로 출력

import sys
from collections import deque

input = sys.stdin.readline

# bfs
def bfs(start, list):
  queue = deque([start])
  
  while queue:
    node = queue.popleft()
    
    if visited[node]:
      continue
  
    visited[node] = 1
    
    if not (set1 & set(list[node])):    # set1에 인접한 노드가 없는 경우
      set1.add(node)
    elif not (set2 & set(list[node])):  # set2에 인접한 노드가 없는 경우
      set2.add(node)
    else:                               # 양 집합 모두 인접 노드가 존재하는 경우
      return False
    
    queue.extend(list[node])
  
  return True

k = int(input())

for _ in range(k):
  v, e = map(int, input().split())
  visited = [0] * (v + 1)
  set1, set2 = set(), set()
  
  # 인접 리스트 생성  
  adjacency_list = [[] for _ in range(v + 1)]
  for _ in range(e):
    v1, v2 = map(int, input().split())
    adjacency_list[v1].append(v2)
    adjacency_list[v2].append(v1)
  
  # 출력
  result = True
  for start in range(1, v + 1):
    if visited[start]:
      continue
    
    result = result and bfs(start, adjacency_list)
  
  if result:
    print('YES')
  else:
    print('NO')