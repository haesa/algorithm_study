import sys
from collections import Counter

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
A = Counter(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for num in B:
  write(str(A[num]) + ' ')
