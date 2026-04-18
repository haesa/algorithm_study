import sys
read = sys.stdin.readline

N, M = map(int, read().split())
nums = list(map(int, read().split()))

d = [0] * (N + 1)
for i in range(1, N + 1):
    d[i] = d[i - 1] + nums[i - 1]

d = list(map(lambda x: x % M, d))

count = 0
s = {}
for x in d:
    if not x in s:
        s[x] = 1
    else:
        count += s[x]
        s[x] += 1

print(count)
