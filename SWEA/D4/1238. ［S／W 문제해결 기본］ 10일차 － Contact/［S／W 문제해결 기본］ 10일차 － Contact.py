from collections import deque, defaultdict

def bfs(start):
    q = deque([(0, start)])
    visited = set()
    visited.add(start)

    result = (0, 0) # (depth, 개인 식별 번호)

    while q:
        depth, cur = q.popleft()

        if result < (depth, cur):
            result = (depth, cur)

        for next in graph[cur]:
            if not next in visited:
                q.append((depth + 1, next))
                visited.add(next)

    return result[1]

for test_case in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(0, N, 2):
        if not arr[i + 1] in graph[arr[i]]:
            graph[arr[i]].append(arr[i + 1])

    ans = bfs(start)
    print(f'#{test_case} {ans}')
