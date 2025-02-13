# 입력: N, M, K (1 <= N <= K <= 10^5, 1 <= M <= 10^9)
# 로직: 
#   1. K개의 맥주 중 N개의 맥주를 선택하여 선호도의 합 M을 채우는 문제
#   2. 선택된 맥주의 도수 레벨의 합이 M 이상이어야 함
#   3. 선택된 맥주의 선호도의 합이 최소가 되어야 함
#     => 최솟값 문제이므로 도수 레벨이 낮은 맥주부터 선택하기 위해 맥주를 도수 레벨이 낮은 순으로 정렬
#     => 순차적으로 맥주를 하나씩 선택하면서 선택된 맥주가 N개인지 확인
#     => 맥주 N개의 선호도 합이 M을 넘는다면 맥주병에 걸리지 않기 위해 마지막으로 선택된 맥주의 도수 레벨을 출력 (선택된 맥주 중 가장 높은 도수 레벨)
#     => 넘지 않는다면 더 빨리 M을 넘기기 위해 만족도가 제일 낮은 맥주를 제거
#     => 위 과정을 반복
#   4. 조건을 만족할 수 없는 경우 -1 출력 (맥주 N개를 선택하지 못 한 경우)
# 출력: 선호도의 합 M을 채우면서 N개의 맥주를 모두 마실 수 있는 간 레벨의 최솟값 (단, 조건을 만족할 수 없는 경우 -1 출력)

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, K = map(int, input().split())
beer_list = [list(map(int, input().split())) for _ in range(K)]

beer_list.sort(key=lambda x: x[1])  # 도수 레벨 기준으로 오름차순 정렬

picked_list = []
total_v = 0

for v, c in beer_list:
  heappush(picked_list, v)
  total_v += v
  
  if len(picked_list) < N:  # 선택된 맥주가 N개보다 적으면 더 선택해야함
    continue
  
  if total_v >= M:  # 선택된 맥주의 도수 레벨 합이 M보다 크거나 같으면 종료
    print(c)  # 마지막으로 선택된 맥주의 도수 레벨 출력
    break
  else:
    total_v -= heappop(picked_list) # 선호도가 가장 낮은 맥주를 제거

if len(picked_list) < N:  # 선택된 맥주가 N개보다 적으면 -1 출력
  print(-1)