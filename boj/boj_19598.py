# 입력: N, 회의 시작 시각 - 종료 시각 (N: 회의 개수)
# 로직:
#   계산을 편하게 하기 위해서 주어진 회의 일정을 시간 순대로 정렬하는 시도를 해볼 수 있다.
#   회의 시작 시각을 기준으로 오름차순 정렬 시 앞의 회의는 현재 회의보다 먼저 진행 중인 것이기 때문에
#   현재 회의의 시작 시각과 앞 회의들의 종료 시각을 비교해야 한다.
#   이때 가장 빨리 끝나는 회의 순으로 비교해야 하기 때문에 최소힙 자료구조를 사용할 수 있다.
#   이미 진행 중인 회의들의 종료 시각을 최소힙에 저장하고 현재 회의의 시작 시각과 비교하여 
#   더 작으면 이미 회의가 종료되었다는 의미이므로 해당 회의 종료 시각을 힙에서 제거해야 한다.
#   그 후 현재 회의 종료 시각을 힙에 추가해야 한다.
#   이때 힙의 크기는 현재 진행 중인 회의 개수이므로 이를 활용하여 최소 회의실 개수를 계산할 수 있다.
#   회의실 개수를 count에 0으로 초기화한 후 매 계산마다 이전 힙의 크기와 비교해서 더 큰 값으로 갱신해야 한다.
# 출력: 최소 회의실 개수

import sys
import heapq

intput = sys.stdin.readline

N = int(input())  # 회의 수
meeting_list = [list(map(int, input().split())) for _ in range(N)]

meeting_list.sort(key=lambda x: x[0])  # 시작 시간 기준으로 정렬
heap = []  # 진행 중인 회의들의 종료 시각
heapq.heapify(heap)

count = 0
for start, end in meeting_list:
  while heap and heap[0] <= start:  # 앞의 회의에서 회의실 사용이 끝난 경우
    heapq.heappop(heap)
  heapq.heappush(heap, end) # 해당 회의 종료 시간 추가
  count = max(count, len(heap)) # 최대 회의실 사용 수 저장

print(count)