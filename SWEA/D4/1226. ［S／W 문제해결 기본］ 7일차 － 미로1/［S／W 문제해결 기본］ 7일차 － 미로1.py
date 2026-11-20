from collections import deque

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y, maze):
    q = deque([(start_x, start_y)])
    visited = [[False] * 16 for _ in range(16)]
    visited[start_y][start_x] = True

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if maze[next_y][next_x] == 3:
                return 1

            if 0 <= next_x < 16 and 0 <= next_y < 16 and maze[next_y][next_x] == 0 and not visited[next_y][next_x]:
                q.append((next_x, next_y))
                visited[next_y][next_x] = True

    return 0

for test_case in range(1, 11):
    T = int(input())

    maze = [list(map(int, input())) for _ in range(16)]

    start_x, start_y = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_y = i
                start_x = j
                break

    print(f'#{test_case} {bfs(start_x, start_y, maze)}')
