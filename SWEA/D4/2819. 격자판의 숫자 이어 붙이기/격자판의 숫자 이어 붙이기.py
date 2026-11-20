# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, number, board, s):
    if r < 0 or r >= 4 or c < 0 or c >= 4:
        return

    number += str(board[r][c])
    if len(number) == 7:
        s.add(number)
        return

    for i in range(4):
        nr = r + dr[i]
        nc =  c + dc[i]
        dfs(nr, nc, number, board, s)

T = int(input())

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]

    s = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, '', board, s)

    print(f'#{test_case} {len(s)}')