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
