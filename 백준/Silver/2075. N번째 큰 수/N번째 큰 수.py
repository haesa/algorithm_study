import sys
import heapq

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

heap = []
for _ in range(N):
  for num in map(int, read().split()):
    if len(heap) < N:
      heapq.heappush(heap, num)
    else:
      heapq.heappushpop(heap, num)

write(str(heap[0]))