# 입력: N, M (회사 컴퓨터의 개수, 컴퓨터간 신롸 관계를 나타내는 간선 정보의 개수)
# 로직:
#   컴퓨터간 신뢰 관계를 인접 리스트로 표현한다.
#   A가 B를 신뢰하면 B는 A를 해킹할 수 있으므로 계산하기 편하게 list[B]에 A를 추가하는 방법을 따른다.
#   1~N을 인접 리스트의 순회 시작점으로 두고 신뢰 관계를 역추적하여 해킹 가능한 컴퓨터 개수를 구한다.
#   해킹 가능한 컴퓨터 개수가 가장 많은 컴퓨터 번호를 result 배열에 저장한다.
# 출력: 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 번호를 오름차순 출력

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
list = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  list[b].append(a)

def bfs(start):
  queue = deque([start])
  visited = [False] * (n + 1)
  visited[start] = True
  count = 1
  
  while queue:
    current = queue.popleft()
    
    for next in list[current]:
      if not visited[next]:
        queue.append(next)
        visited[next] = True
        count += 1

  return count

result = []
max_value = 0

for i in range(1, n + 1):
  value = bfs(i)
  
  if max_value > value:
    continue
  
  if max_value < value:
    max_value = value
    result.clear()
    
  result.append(i)

print(*result)