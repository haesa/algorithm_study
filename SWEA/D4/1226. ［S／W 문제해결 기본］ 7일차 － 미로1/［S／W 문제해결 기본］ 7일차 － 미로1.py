from collections import deque

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y, maze):
    q = deque([(start_x, start_y)])
    maze[start_y][start_x] = 1

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x < 0 or next_x >= 16 or next_y < 0 or next_y >= 16:
                continue

            if maze[next_y][next_x] == 3:
                return 1

            if maze[next_y][next_x] == 0:
                q.append((next_x, next_y))
                maze[next_y][next_x] = 1

    return 0

for test_case in range(1, 11):
    T = int(input())

    maze = [list(map(int, input())) for _ in range(16)]

    start_x, start_y = 0, 0
    for i in range(16):
        if 2 in maze[i]:
            start_y = i
            start_x = maze[i].index(2)
            break

    print(f'#{test_case} {bfs(start_x, start_y, maze)}')
