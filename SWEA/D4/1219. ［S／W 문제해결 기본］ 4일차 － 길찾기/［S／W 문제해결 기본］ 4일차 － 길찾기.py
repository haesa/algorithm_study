from collections import deque, defaultdict

def bfs(graph):
    q = deque([0])
    visited = set()
    visited.add(0)

    while q:
        node = q.popleft()

        for next in graph[node]:
            if next == 99:
                return 1
            if not next in visited:
                q.append(next)
                visited.add(next)

for test_case in range(1, 11):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(N):
        graph[arr[i * 2]].append(arr[i * 2 + 1])

    if bfs(graph):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')