# 입력: T, N, 서류,면접 심사 순위 (T: 테스트 케이스 수, N: 지원자 수) 
# 로직:
#   1. 서류심사 순위로 정렬하면 뒤에 있는 지원자들보다 서류 순위는 높기 때문에 앞에 있는 지원자들의 면접 순위만 비교하면 된다.
#   2. 최종 선발되기 위해선 나보다 서류심사 순위가 높은 사람들보다 면접 순위가 높아야한다.
#   3. highest_rank에 가장 높은 면접 순위를 담아 나의 면접 순위와 비교한다.
#   4. 나의 순위가 더 높다면 최종 합격이다.
#   5. count에 1을 더하고 highest_rank를 나의 순위로 갱신한다.
#   6. 서류심사 1등은 무조건 선발되기 때문에 count = 1로 시작한다.
# 출력: 선발할 수 있는 신입사원의 최대 인원수

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  rank_list = [list(map(int, input().split())) for _ in range(N)]
  rank_list.sort() # 서류심사 순위로 정렬
  count = 1 # 선발된 지원자의 수 (서류심사 1등은 무조건 선발)
  
  highest_rank = rank_list[0][1] # 서류심사 1등의 면접심사 순위
  for i in range(N):
    if rank_list[i][1] < highest_rank: # 서류심사 순위가 더 높은 지원자들의 면접심사 순위보다 더 높으면 합격
      count += 1
      highest_rank = rank_list[i][1]
  
  print(count)  # 선발되 지원자 수 출력