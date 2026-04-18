import sys
read = sys.stdin.readline

T = int(read())

for t in range(T):
    P = int(read())

    DP = [0] * (P + 1)
    if 1 <= P <= 3:
        print(1)
        continue
    elif 4 <= P <= 5:
        print(2)
        continue
    else:
        DP[1] = DP[2] = DP[3] = 1
        DP[4] = DP[5] = 2
        for i in range(6, P + 1):
            DP[i] = DP[i - 1] + DP[i - 5]
        print(DP[P])
