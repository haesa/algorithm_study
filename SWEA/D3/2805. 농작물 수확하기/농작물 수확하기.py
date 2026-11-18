T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    mid = (N - 1) // 2
    result = 0

    for i in range(N):
        for j in range(abs(mid - i), N - abs(mid - i)):
            result += board[i][j]

    print(f'#{test_case} {result}')
