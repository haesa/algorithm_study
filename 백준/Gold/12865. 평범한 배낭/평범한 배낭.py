import sys
read = sys.stdin.readline

N, K = map(int, read().split())
input_list = []
for _ in range(N):
    W, V = map(int, read().split())
    input_list.append((W, V))

input_list.sort()
DP = [0] * (K + 1)

for w, v in input_list:
    for i in range(K, w - 1, -1):
        DP[i] = max(DP[i], DP[i - w] + v)

print(DP[K])
