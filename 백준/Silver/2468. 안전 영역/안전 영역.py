import sys
from collections import deque

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]

# offset (위쪽부터 시작 -> 시계방향)
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid_boundary(r, c):
    return r >= 0 and r < N and c >= 0 and c < N


# O(V + E) -> O(N^2)
def dfs(r, c, h, visited):
    q = deque([(r, c)])
    visited[r][c] = 1

    while q:
        cur_r, cur_c = q.popleft()

        for dr, dc in d:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if not is_valid_boundary(next_r, next_c) or visited[next_r][next_c] or graph[next_r][next_c] <= h:
                continue

            q.append((next_r, next_c))
            visited[next_r][next_c] = 1


def solution():
    result = 1  # 비가 오지 않은 경우는 안전 영역의 개수가 1
    graph_flatten = [h for row in graph for h in row]
    water_level_list = list(set(graph_flatten))  # 각 영역의 높이

    for h in water_level_list:
        # 방문 여부 확인
        visited = [[0] * N for _ in range(N)]
        count = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] or graph[i][j] <= h:
                    continue
                # 방문하지 않고, 침수되지 않은 노드로 시작
                dfs(i, j, h, visited)
                count += 1
        result = count if count > result else result
    return result


write(str(solution()))
