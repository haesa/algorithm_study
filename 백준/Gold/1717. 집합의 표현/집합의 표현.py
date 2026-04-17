import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N, M = map(int, read().split())
input_list = [map(int, read().split()) for _ in range(M)]

parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root


for cmd, a, b in input_list:
    if cmd == 0:
        union(a, b)
    elif cmd == 1:
        print('YES' if find(a) == find(b) else 'NO')
