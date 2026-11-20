from collections import deque

def bfs(graph):
    q = deque([0])
    visited = [False] * 100
    visited[0] = True

    while q:
        node = q.popleft()

        for next in graph[node]:
            if next == 99:
                return 1

            if not visited[next]:
                q.append(next)
                visited[next] = True

    return 0

for test_case in range(1, 11):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(100)]

    for i in range(0, N * 2, 2):
        graph[arr[i]].append(arr[i + 1])

    print(f'#{test_case} {bfs(graph)}')