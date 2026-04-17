import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  rank_list = [list(map(int, input().split())) for _ in range(N)]
  rank_list.sort() # 서류심사 순위로 정렬
  count = 1 # 선발된 지원자의 수
  
  highest_rank = rank_list[0][1] # 서류심사 1등의 면접심사 순위
  for i in range(N):
    if rank_list[i][1] < highest_rank: # 서류심사 순위가 더 높은 지원자들의 면접심사 순위보다 더 높으면 합격
      count += 1
      highest_rank = rank_list[i][1]
  
  print(count)  # 선발되 지원자 수 출력