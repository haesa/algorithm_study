import sys
import heapq

read = sys.stdin.readline
write = sys.stdout.write

N, K = list(map(int, read().split()))
gem_list = [list(map(int, read().split())) for _ in range(N)]
bag_list = [int(read()) for _ in range(K)]

gem_list.sort(key = lambda x: x[0])
bag_list.sort()

heap = []
result = 0
i = 0

for capacity in bag_list:
  while i < N and capacity >= gem_list[i][0]:
    heapq.heappush(heap, -gem_list[i][1])
    i += 1
  
  if heap:
    result += -heapq.heappop(heap)

write(str(result))