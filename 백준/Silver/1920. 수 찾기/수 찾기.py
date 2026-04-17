import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = []
for num in B:
    result.append('1' if num in A else '0')
write('\n'.join(result))