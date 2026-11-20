def dfs(r):
    if r == N:
        return 1

    ans = 0
    for c in range(N):
        can = True
        for qr, qc in queens:
            if c == qc:
                can = False
                break
            if abs(qr - r) == abs(qc - c):
                can = False
                break

        if can:
            queens.append((r, c))
            ans += dfs(r + 1)
            queens.pop()

    return ans

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    queens = []
    ans = dfs(0)

    print(f'#{test_case} {ans}')
