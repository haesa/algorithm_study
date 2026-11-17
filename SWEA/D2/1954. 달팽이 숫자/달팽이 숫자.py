T = int(input())

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]

    r, c = 0, 0
    d = 0
    for val in range(1, N * N + 1):
        board[r][c] = val

        # 범위 밖이거나 이미 채워진 칸이면 방향 전환
        nr = r + dr[d]
        nc = c + dc[d] 
        if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc]:
            d = (d + 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
        r, c = nr, nc

    print(f'#{test_case}')
    for row in board:
        print(*row)