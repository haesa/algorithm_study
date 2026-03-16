import sys
read = sys.stdin.readline

N, M = map(int, read().split())

S = set([read().strip() for _ in range(N)])
count = 0
for _ in range(M):
  s = read().strip()
  if s in S:
    count += 1
print(count)
