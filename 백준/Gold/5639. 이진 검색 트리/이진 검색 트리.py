import sys
sys.setrecursionlimit(10**6)

read = sys.stdin.readline
write = sys.stdout.write

graph = []
while True:
    node = read().strip()
    if not node:  # EOF
        break

    graph.append(int(node))

N = len(graph)


def dfs(start, end):
    if start > end:
        return []

    if start == end:
        return [graph[start]]

    root = graph[start]
    i = start + 1
    while i <= end and root > graph[i]:
        i += 1

    result = []
    result.extend(dfs(start + 1, i - 1))
    result.extend(dfs(i, end))
    result.append(root)

    return result


write('\n'.join(map(str, dfs(0, N - 1))))
