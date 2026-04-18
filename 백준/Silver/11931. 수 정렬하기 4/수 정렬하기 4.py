import sys

t = int(sys.stdin.readline())
numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline().strip()))

numbers.sort(reverse=True)
print(*numbers, sep='\n')