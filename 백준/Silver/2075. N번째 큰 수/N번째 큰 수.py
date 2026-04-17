import sys
import heapq

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

heap = []
for _ in range(N):
  for num in list(map(int, read().split())):
    if len(heap) >= N:
      heapq.heappushpop(heap, num)
    else:
      heapq.heappush(heap, num)

write(str(heapq.heappop(heap)))