import sys
from collections import deque
read = sys.stdin.readline

N = int(read().strip())
graph = [list(map(int, read().rstrip())) for _ in range(N)]

visitted = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def valid_boundary(r, c):
    return r >= 0 and r < N and c >= 0 and c < N


def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    visitted[start_r][start_c] = 1
    count = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if valid_boundary(nr, nc) and graph[nr][nc] and not visitted[nr][nc]:
                q.append((nr, nc))
                visitted[nr][nc] = 1
                count += 1
    return count


answer = []
count = 0
for i in range(N):
    for j in range(N):
        if not graph[i][j]:
            continue
        if not visitted[i][j]:
            answer.append(bfs(i, j))
            count += 1

print(count, *sorted(answer), sep='\n')
