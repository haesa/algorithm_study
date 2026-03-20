import sys
read = sys.stdin.readline

N, M = map(int, read().split())
nums = list(map(int, read().split()))

'''
구간: (i, j)
(d[j] - d[i - 1]) % M = 0
d[j] % M = d[i - 1] % M
'''

d = [0] * (N + 1)
r = [0] * M
for i in range(1, N + 1):
    d[i] = d[i - 1] + nums[i - 1]
    r[d[i] % M] += 1
r[0] += 1  # d[0] % M

count = 0
for x in r:
    count += x * (x - 1) // 2
print(count)
