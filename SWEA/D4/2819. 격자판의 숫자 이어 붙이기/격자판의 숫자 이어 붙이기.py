# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, number, depth):
    number = number * 10 + board[r][c]

    if depth == 6:
        numbers.add(number)
        return

    for i in range(4):
        nr = r + dr[i]
        nc =  c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, number, depth + 1)

T = int(input())

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]

    numbers = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j,0, 0)

    print(f'#{test_case} {len(numbers)}')