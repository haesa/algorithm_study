import sys
read = sys.stdin.readline

N, M = map(int, read().split())
nums = list(map(int, read().split()))

d = [0] * N
d[0] = nums[0]
for i in range(1, N):
  d[i] = d[i - 1] + nums[i]

for _ in range(M):
  a, b = map(int, read().split())
  if a==1:
    print(d[b - 1])
  else:
    print(d[b - 1] - d[a - 2])
