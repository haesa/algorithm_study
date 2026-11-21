N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

ans = [0] * 3

def solution(start, end, n):
    s = set()
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            s.add(paper[i][j])

    if len(s) == 1:
        ans[paper[start[0]][start[1]] + 1] += 1
        return

    for i in range(start[0], end[0] + 1, n // 3):
        for j in range(start[1], end[1] + 1, n // 3):
            solution((i, j), (i + n // 3 - 1, j + n // 3 - 1), n // 3)

solution((0, 0), (N - 1, N - 1), N)
for x in ans:
    print(x)