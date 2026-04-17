import sys
from collections import defaultdict

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
graph = defaultdict(list)
for _ in range(N):
    parent, left, right = read().split()
    graph[parent].append(left)
    graph[parent].append(right)


def preorder(graph, start):
    if start == '.':
        return ''

    path = ''
    for next in graph[start]:
        path += preorder(graph, next)

    return start + path


def inorder(graph, start):
    if start == '.':
        return ''

    left, right = graph[start]

    path = ''
    path += inorder(graph, left)
    path += start
    path += inorder(graph, right)

    return path


def postorder(graph, start):
    if start == '.':
        return ''

    path = ''
    for next in graph[start]:
        path += postorder(graph, next)

    return path + start


write(preorder(graph, 'A'))
write('\n')
write(inorder(graph, 'A'))
write('\n')
write(postorder(graph, 'A'))
