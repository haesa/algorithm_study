T = int(input())

# 우 하 좌 상
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for test_case in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]

    i, j = 0, 0
    d = 0
    for val in range(1, N * N + 1):
        board[i][j] = val

        # 범위 밖이거나 이미 채워진 칸이면 방향 전환
        dr, dc = direction[d]
        if i + dr >= N or j + dc >= N or board[i + dr][j + dc] > 0:
            d = (d + 1) % 4
        dr, dc = direction[d]
        i += dr
        j += dc

    print(f'#{test_case}')
    for row in board:
        print(*row)