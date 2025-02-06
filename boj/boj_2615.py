# 입력: 검은 바둑알과 흰 바둑알이 놓여져 있는 19 X 19 크기의 바둑판
# 로직:
#   바둑판을 graph에 저장한다.
#   가로줄 r, 세로줄 c라고 두었을 때 (r, c)에 대한 → ↓ ↘ ↗ 방향으로 오목을 탐색한다.
#   육목은 승리로 인정하지 않기 때문에 오목인 경우 육목 체크를 해야한다.
#   육목인 경우 다른 방향으로 탐색을 이어간다.
#   육목이 아닌 경우 graph[r][c]을 출력하고, r + 1과 c + 1을 출력한다.
#   바둑판을 모두 탐색했는데도 승부가 나지 않았다면 0을 출력한다.
# 출력: 
#   첫 째줄: 검은 돌이 이기면 1, 흰 돌이 이기면 2, 승부가 나지 않은 경우 0
#   둘 째줄: 제일 왼쪽에 있는 바둑알의 가로줄, 세로줄 위치 (세로로 놓인 경우 가장 위에 있는 바둑알 위치)

import sys

input = sys.stdin.readline

# → ↓ ↘ ↗
dr = [0, 1, 1, -1]
dc = [1, 0, 1, 1]

# 인덱스 유효성 검사
def valid_range(r, c):
  return 0<= r < 19 and 0 <= c < 19

def solve():
  for r in range(19):
    for c in range(19):
      if graph[r][c] == 0:
        continue
      
      focus = graph[r][c]
      
      for k in range(4):
        # 한 방향으로 연속적으로 색이 동일한 바둑알 수
        count = 1 
        
        # 다음 바둑알
        nr = r + dr[k]
        nc = c + dc[k]
        
        while valid_range(nr, nc) and graph[nr][nc] == focus: # 이전 바둑알과 색이 일치하는 경우
          count += 1
          
          if count == 5:  # 오목인 경우 육목 체크
            if valid_range(r - dr[k], c - dc[k]) and graph[r - dr[k]][c - dc[k]] == focus: # 왼쪽 바둑알 검사
              break
            
            if valid_range(nr + dr[k], nc + dc[k]) and graph[nr + dr[k]][nc + dc[k]] == focus: # 오른쪽 바둑알 검사
              break
            
            # 출력
            print(focus)
            print(r + 1, c + 1)
            return True
          
          # 동일한 방향으로 다음 바둑알로 이동
          nr += dr[k]
          nc += dc[k]

  return False

# 바둑판 입력
graph = []
for _ in range(19):
  graph.append(list(map(int, input().split())))

result = solve()

if result == False:
  print(0)