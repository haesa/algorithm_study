import sys
import heapq
read = sys.stdin.readline

heap = []
N = int(read().rstrip())
for _ in range(N):
    cmd = int(read().rstrip())

    if cmd == 0:
        print(heapq.heappop(heap) if len(heap) > 0 else 0)
    elif cmd > 0:
        heapq.heappush(heap, cmd)
